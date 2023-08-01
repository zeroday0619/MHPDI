import uvicorn
from api import root

from fastapi import FastAPI

app = FastAPI()
app.include_router(router=root, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)