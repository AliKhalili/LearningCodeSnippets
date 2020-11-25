import datetime

from sqlalchemy import Column, Integer, DATETIME, String
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, BigInteger


def resolve_table_name(name):
    """Resolves table names to their mapped names."""
    names = re.split("(?=[A-Z])", name)  # noqa
    return "_".join([x.lower() for x in names if x])


class CustomBase:
    @declared_attr
    def __tablename__(self):
        return resolve_table_name(self.__name__)

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    create_date = Column(DATETIME, default=datetime.datetime.utcnow)


Base = declarative_base(cls=CustomBase)
