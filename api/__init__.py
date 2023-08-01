from fastapi import APIRouter
from api.geo import geo_root

root = APIRouter()
root.include_router(router=geo_root, prefix="/geo")