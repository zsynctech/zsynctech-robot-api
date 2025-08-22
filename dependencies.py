from fastapi import Header, HTTPException

API_TOKEN = "1234567890"

def verify_bearer_token(authorization: str = Header(...)):
    """
    Verifica se o header Authorization contém o token correto no formato:
    Authorization: Bearer <token>
    """
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authorization inválido")
    
    token = authorization.split(" ", 1)[1]
    if token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Token inválido")
    return True