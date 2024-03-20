from pydantic import BaseModel, Field
from .organization import Organization


class ResponseGet(BaseModel):
    data: Organization = Field(default=None, alias='organization')
