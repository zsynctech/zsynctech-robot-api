from fastapi import APIRouter, Response, HTTPException
import json
from settings import (
    COMPUTERNAME,
    IP_ADDRESS,
    CACHE
)

router = APIRouter(
    tags=["health"],
    responses={
        404: {
            "description": "Not found"
        }
    }
)

@router.get("/{instance_id}/health")
def health(instance_id: str):
    instance = CACHE.get(instance_id)

    if not instance:
        raise HTTPException(
            status_code=404,
            detail="Not found"
        )

    return Response(
        status_code=200,
        content=json.dumps({
            "machine_info": {
                "IP_ADDRESS": IP_ADDRESS,
                "COMPUTERNAME": COMPUTERNAME
            }
        }),
        media_type="application/json"
    )
