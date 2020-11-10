from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data.model.base import Base
from data.model.meta_model import MetaModel


class Repository:
    def __init__(self, configuration):
        self._engine = create_engine('sqlite:///D:\\_temp_python\\foo.db', echo=True)
        self._session = sessionmaker(bind=self._engine)()
        Base.metadata.create_all(self._engine)

    def add(self, entity: Base):
        self._session.add(entity)

    def get(self, key: str):
        self._session.query(MetaModel).filterby(key=key).first()

    def save_change(self):
        try:
            self._session.commit()
        except Exception as ex:
            self._session.rollback()
            return False
        return True

    @contextmanager
    def get_context(self):
        try:
            yield self
            self._session.commit()
        except Exception as ex:
            self._session.rollback()


db = Repository()
