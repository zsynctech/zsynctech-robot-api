from fastapi import APIRouter, Response, HTTPException, Depends, BackgroundTasks
from dependencies import verify_bearer_token
from models.instances import InstanceData
from settings import RABBITMQ_URL
import json
import pika

router = APIRouter(
    tags=["start"],
    responses={
        404: {
            "description": "Not found"
        }
    }
)

EXCHANGE_NAME = "start"

def send_to_queue(instance_id: str, data: dict):
    try:
        connection = pika.BlockingConnection(
            pika.URLParameters(url=RABBITMQ_URL)
        )
        channel = connection.channel()
        channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='direct', durable=True)
        channel.basic_publish(
            exchange=EXCHANGE_NAME,
            routing_key=f"instance.{instance_id}",
            body=json.dumps(data),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )
        connection.close()
    except Exception as e:
        print(f"[RabbitMQ] Erro ao enviar mensagem: {e}")


@router.post("/{instance_id}/start", dependencies=[Depends(verify_bearer_token)])
def start(
        instance_data: InstanceData,
        background_tasks: BackgroundTasks
    ):
    try:
        background_tasks.add_task(send_to_queue, instance_data.instanceId, instance_data.model_dump())
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao enviar dados da execução")

    return Response(
        status_code=200,
        content=json.dumps({"message": "Instance started"}),
        media_type="application/json"
    )