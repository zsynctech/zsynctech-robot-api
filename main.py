from routes import health, start
from fastapi import FastAPI

app = FastAPI(
    title="API ZSync Tech",
    description="API para gerenciamento de instâncias de automações",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(start.router)
