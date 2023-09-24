import uvicorn
from api import root
from src.loader import DATALoader
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["https://mental.menhera.kr"],
        allow_credentials=True,
        allow_methods=["GET"],
    )
]


app = FastAPI(
   middleware=middleware, 
)
app_data = DATALoader()
app.include_router(router=root, prefix="/api")


@app.get("/")
async def read_root():
    return {"message": True}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)