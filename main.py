import uvicorn

from fastapi import FastAPI

from api.clients import api_router
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix='/api')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
