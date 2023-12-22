from pydantic import BaseModel, Field
from .people import People


class ResponseGet(BaseModel):
    people: People = Field(default=None, alias='person')
