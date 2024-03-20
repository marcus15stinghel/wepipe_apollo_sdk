from pydantic import BaseModel, Field
from typing import List
from .contact import Contact


class ResponseGet(BaseModel):
    data: List[Contact] = Field(default=None, alias='contacts')
