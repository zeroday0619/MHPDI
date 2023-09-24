import uvicorn
from api import root
from src.loader import DATALoader
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app_data = DATALoader()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://mental.menhera.kr"],
    allow_credentials=True,
)
app.include_router(router=root, prefix="/api")


@app.get("/")
async def read_root():
    return {"message": True}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)