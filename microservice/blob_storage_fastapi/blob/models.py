from typing import Optional

from models import BaseModel
from utils import random_generator


class MetaBase(BaseModel):
    key: Optional[str]
    file_name: Optional[str]
    content_type: Optional[str]


class MetaCreate(MetaBase):
    def __init__(self):
        super(MetaCreate, self).__init__()
        self.key = random_generator()


class MetaRead(MetaBase):
    pass
