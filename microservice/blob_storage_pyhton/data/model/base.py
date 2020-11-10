import datetime

from sqlalchemy import Column, Integer, DATETIME
from sqlalchemy.ext.declarative import declarative_base, declared_attr


class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    create_date = Column(DATETIME, default=datetime.datetime.utcnow)


Base = declarative_base(cls=Base)
