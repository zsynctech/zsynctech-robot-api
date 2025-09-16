from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import HTTPException, Depends
from settings import TOKENS
import json


if TOKENS is None:
    raise RuntimeError("Tokens não encontrados")

TOKENS = json.loads(TOKENS)

security = HTTPBearer()

def verify_bearer_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Verifica se o header Authorization contém o token correto no formato:
    Authorization: Bearer <token>
    """

    if str(credentials.scheme).lower().strip() != "bearer":
        raise HTTPException(status_code=401, detail="Authorization inválido")

    if credentials.credentials not in TOKENS:
        raise HTTPException(status_code=401, detail="Token inválido")
    return True