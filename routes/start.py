from fastapi import APIRouter, Response, HTTPException, Depends
from dependencies import verify_bearer_token
from models.instances import InstanceData
from settings import SDK_DIR
import json
import os

router = APIRouter(
    tags=["start"],
    responses={
        404: {
            "description": "Not found"
        }
    }
)

@router.post("/{instance_id}/start", dependencies=[Depends(verify_bearer_token)])
def start(instance_data: InstanceData):
    try:
        instance_path = os.path.join(SDK_DIR, instance_data.instanceId)
        os.makedirs(instance_path, exist_ok=True)
        file_path = os.path.join(instance_path, f"{instance_data.instanceId}.json")

        with open(file_path, mode="w", encoding="utf8") as file:
            json.dump(instance_data.model_dump(), file, ensure_ascii=False, indent=4)

    except PermissionError:
        raise HTTPException(status_code=500, detail="Sem permissão para criar arquivos")
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao criar pasta da instância")

    return Response(
        status_code=200,
        content=json.dumps({"message": "Instance started"}),
        media_type="application/json"
    )