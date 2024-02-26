from typing import TypeVar, Generic, List
from pydantic import BaseModel as _BaseModel, ConfigDict, conint
from pydantic.alias_generators import to_camel

T = TypeVar("T")

class BaseModel(_BaseModel):
    """ Extension of Pydantic's BaseModel to enable ORM extension """
    model_config = ConfigDict(
        # Allow transform from ORM models
        from_attributes = True,
        # Translate Python snake case fields to JS camel case
        alias_generator = to_camel,
        populate_by_name=True
    )

class PageParams(BaseModel):
    page: conint(ge=1) = 1
    size: conint(ge=1, le=100) = 10

class PagedResponse(BaseModel, Generic[T]):
    total: int
    page: int
    size: int
    results: List[T]
