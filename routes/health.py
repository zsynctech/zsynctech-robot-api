from fastapi import APIRouter, Response
import json

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
    return Response(
        status_code=200,
        content=json.dumps({"message": "OK"}),
        media_type="application/json"
    )
