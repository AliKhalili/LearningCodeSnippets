from pydantic.main import BaseModel


class BaseModel(BaseModel):
    class Config:
        orm_mode = True
        validate_assignment = True