import logging
from starlette.requests import Request

from sqlalchemy import create_engine, Column, String, BigInteger
from sqlalchemy.orm import sessionmaker

from config import SQLALCHEMY_DATABASE_URI
from data.entity import Base

log = logging.getLogger(__file__)
engine = create_engine(str(SQLALCHEMY_DATABASE_URI), connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def get_db(request: Request):
    return request.state.db
