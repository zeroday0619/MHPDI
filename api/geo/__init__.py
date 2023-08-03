import os
import math
import json
from src import Geodistance
from src.ncp import NCP
from src.loader import DATALoader
from src.utils import distance
from fastapi import APIRouter, Query

loader = DATALoader()
ncp_app = NCP()
geo_root = APIRouter()

@geo_root.get("/recommend")
async def recommend(
    lat: float = Query(..., description="latitude of point"),
    lon: float = Query(..., description="longitude of point"),
):

    chunk_data = dict()
    try:
        geo_code = ncp_app.reverse_geocode(lat, lon)
    except IndexError:
        return {
            "status": False,
            "message": "지원하지 않는 지역입니다."
        }

    for index in loader.list_files():
        if {*index.keys()}.pop() == geo_code["area1"]:
            chunk_data = index
    data = dict()
    with open(chunk_data[geo_code["area1"]], "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    
    ps_data = list()

    for index_hs in data:
        index_hs["주소"]["distance"] = await distance(
            lat1=lat,
            lon1=lon,
            lat2=float(index_hs["주소"]["위도"]),
            lon2=float(index_hs["주소"]["경도"])
        )
        ps_data.append(index_hs)
    ps_data.sort(key=lambda x: x["주소"]["distance"])
    return {
        "status": True,
        "source": ps_data
    }

