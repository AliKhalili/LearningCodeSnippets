import logging

from fastapi import FastAPI, Depends
import uvicorn
from starlette.applications import Starlette

from api import api_router
from data.database import get_db
from middleware import SetDbMiddleware

log = logging.getLogger(__name__)

app = Starlette()
api = FastAPI()
app.add_middleware(SetDbMiddleware)

api.include_router(api_router, prefix="/v1")

app.mount("/api", app=api)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
