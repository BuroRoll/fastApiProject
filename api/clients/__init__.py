from fastapi import APIRouter

from api.clients import clients

api_router = APIRouter()
api_router.include_router(clients.router, prefix="/clients")
