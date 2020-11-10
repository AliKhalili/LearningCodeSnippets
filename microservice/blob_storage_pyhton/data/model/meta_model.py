from sqlalchemy import Column, String, BigInteger

from data.model.base import Base


class MetaModel(Base):
    __tablename__ = 'Metas'

    key = Column(String, nullable=False, unique=True)
    file_name = Column(String, nullable=False)
    content_disposition = Column(String, nullable=False)
    content_type = Column(String, nullable=False)
    length = Column(BigInteger, nullable=False)
    path = Column(String, nullable=True)

    def __repr__(self):
        return f'<{self.__tablename__}(id={self.id}, key={self.key}, path={self.path})>'
