from pydantic import BaseModel, Field
from .data import Data


class ResponseGet(BaseModel):
    data: Data = Field(default=None, alias='person')
