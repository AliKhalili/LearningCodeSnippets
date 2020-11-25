from typing import Optional

from sqlalchemy.orm import Session

from blob.models import MetaModel, MetaModelCreate


def get_by_id(*, db_session: Session, meta_id: int) -> Optional[MetaModel]:
    """Fetch a meta by it's `meta_id`."""
    return db_session.query(MetaModel).filter(MetaModel.id == meta_id).one()


def get_by_key(*, db_session: Session, meta_key: str) -> Optional[MetaModel]:
    """Fetch a meta by it's `meta_key`."""
    return db_session.query(MetaModel).filter(MetaModel.key == meta_key).one()


def delete(*, db_session: Session, meta_id: int):
    meta = db_session.query(MetaModel).filter(MetaModel.id == meta_id).one_or_none()
    db_session.delete(meta)
    db_session.commit()


def create(*, db_session: Session, meta_in: MetaModelCreate):
    meta = MetaModel(**meta_in.dict())
    db_session.add(meta)
    db_session.commit()
    db_session.flush(meta)
    return meta
