from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID

class InstanceConfig(BaseModel):
    instance_id: str = Field(..., description="ID da instância")
    script: str = Field(..., description="Caminho do script Python")
    runner: str = Field(..., description="Comando para executar o script, ex: 'uv run' ou 'python'")
    token: str = Field(..., description="Token de autenticação")


class ConfigModel(BaseModel):
    instances: List[InstanceConfig] = Field(..., description="Lista de instâncias")


class Credential(BaseModel):
    key: str
    value: str
    encrypted: bool


class InstanceData(BaseModel):
    instanceId: str
    automationName: str
    clientId: str
    userId: str
    executionId: str
    inputPath: str
    inputMetaData: Optional[dict] = None
    inputType: str
    outputPath: str
    outputMetaData: Optional[dict] = None
    outputType: str
    keepAlive: bool
    keepAliveInterval: Optional[int] = None
    credentials: Optional[List[Credential]] = None