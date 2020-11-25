import logging
from starlette.requests import Request

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import SQLALCHEMY_DATABASE_URI

log = logging.getLogger(__file__)
engine = create_engine(str(SQLALCHEMY_DATABASE_URI), connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(bind=engine)


def get_db(request: Request):
    return request.state.db
