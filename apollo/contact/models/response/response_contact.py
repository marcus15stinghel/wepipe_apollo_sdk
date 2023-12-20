from pydantic import BaseModel, Field
from .data import Data


class ResponseContact(BaseModel):
    data: Data = Field(default=None, alias='person')
