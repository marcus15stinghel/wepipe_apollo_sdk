from pydantic import BaseModel, Field
from .organization import Organization


class ResponseGet(BaseModel):
    organization: Organization = Field(default=None, alias='organization')
