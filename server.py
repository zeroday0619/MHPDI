import uvicorn
from api import root
from src.loader import DATALoader
from fastapi import FastAPI

app = FastAPI()
app_data = DATALoader()
app.include_router(router=root, prefix="/api")


@app.get("/")
async def read_root():
    return {"message": app_data.list_files()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)