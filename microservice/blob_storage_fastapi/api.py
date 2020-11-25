from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from data.database import get_db

api_router = APIRouter(
    default_response_class=JSONResponse
)


# api_router.include_router(blob_router, prefix="/blob", tags=["users"])


@api_router.get("/healthcheck", include_in_schema=True)
def healthcheck(db_session: Session = Depends(get_db)):
    database_working = 'ok'
    try:
        db_session.execute('SELECT 1')
    except Exception as e:
        database_working = str(e)
        is_database_working = False
    return {"status": "ok", "db": database_working}
