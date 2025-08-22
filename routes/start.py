from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import APIRouter, Response, HTTPException, Depends
from models.instances import InstanceData
from pydantic import BaseModel
from settings import CACHE
import subprocess
import json
import os

security = HTTPBearer()

router = APIRouter(
    tags=["start"],
    responses={
        404: {
            "description": "Not found"
        }
    }
)

def verify_instance_token(
    instance_id: str,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    instance = CACHE.get(instance_id)
    if not instance:
        raise HTTPException(status_code=404, detail="Instance not found")

    expected_token = getattr(instance, "token", None)
    if not expected_token or credentials.credentials != expected_token:
        raise HTTPException(status_code=401, detail="Invalid token")

    return instance


@router.post("/{instance_id}/start")
def start(instance_data: InstanceData, instance: dict = Depends(verify_instance_token)):
    try:
        print(instance_data)
        args = instance_data.model_dump_json()
        args = args.replace('"', '\\"')

        subprocess.Popen(
            f'{instance.runner} "{instance.script}" -d "{args}"',
            cwd=os.path.dirname(instance.script),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=e.stderr)

    return Response(
        status_code=200,
        content=json.dumps({
            "message": "Instance started"
        }),
        media_type="application/json"
    )
