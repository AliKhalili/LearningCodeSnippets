from typing import Optional

from sqlalchemy.orm import Session

from blob.models import MetaCreate
from data.entity import Meta


def get_by_id(*, db_session: Session, meta_id: int) -> Optional[Meta]:
    """Fetch a meta by it's `meta_id`."""
    return db_session.query(Meta).filter(Meta.id == meta_id).one()


def get_by_key(*, db_session: Session, meta_key: str) -> Optional[Meta]:
    """Fetch a meta by it's `meta_key`."""
    return db_session.query(Meta).filter(Meta.key == meta_key).one()


def delete(*, db_session: Session, meta_id: int):
    meta = db_session.query(Meta).filter(Meta.id == meta_id).one_or_none()
    db_session.delete(meta)
    db_session.commit()


def create(*, db_session: Session, meta_in: MetaCreate) -> Meta:
    meta = Meta(**meta_in.dict())
    meta.length = 0
    db_session.add(meta)
    db_session.commit()
    return meta
