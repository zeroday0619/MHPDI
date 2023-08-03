import os
import httpx


class NCP:
    """NAVER Cloud Platform API"""
    def __init__(self):
        self.REVERSE_GEOCODE_API_URL = "https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc"
        self.NCP_REVERSE_GEO_API_KEY_ID = os.getenv("NCP_REVERSE_GEO_API_KEY_ID")
        self.NCP_REVERSE_GEO_API_KEY = os.getenv("NCP_REVERSE_GEO_API_KEY")
    
    def reverse_geocode(self, lat: float, lng: float) -> dict:
        headers = {
            "X-NCP-APIGW-API-KEY-ID": self.NCP_REVERSE_GEO_API_KEY_ID,
            "X-NCP-APIGW-API-KEY": self.NCP_REVERSE_GEO_API_KEY
        }
        params = {
            "request": "coordsToaddr",
            "coords": f"{lng},{lat}",
            "sourcecrs": "epsg:4326",
            "output": "json",
            "orders": "legalcode"
        }
        with httpx.Client(headers=headers) as client:
            response = client.get(self.REVERSE_GEOCODE_API_URL, params=params)
        resp_json = response.json()
        area1 = resp_json["results"][0]["region"]["area1"]["name"]
        area2 = resp_json["results"][0]["region"]["area2"]["name"]
        area3 = resp_json["results"][0]["region"]["area3"]["name"]
        return {
            "area1": area1,
            "area2": area2,
            "area3": area3,
        }