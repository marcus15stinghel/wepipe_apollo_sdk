from pydantic import BaseModel, Field
from .people import People


class ResponseGet(BaseModel):
    data: People = Field(default=None, alias='person')
