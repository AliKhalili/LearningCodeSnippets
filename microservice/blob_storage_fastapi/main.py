from starlette.responses import JSONResponse
from tabulate import tabulate

import logging

from fastapi import FastAPI, Depends
import uvicorn
from starlette.applications import Starlette

from api import api_router
from logger import configure_logging
from middleware import SetDbMiddleware

log = logging.getLogger(__name__)
configure_logging()

app = Starlette()
api = FastAPI(default_response_class=JSONResponse)
app.add_middleware(SetDbMiddleware)

api.include_router(api_router, prefix="/v1")

app.mount("/api", app=api)

table = []
for r in api_router.routes:
    table.append([r.path, ",".join(r.methods)])

log.debug("Available Endpoints \n" + tabulate(table, headers=["Path", "Methods"]))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
