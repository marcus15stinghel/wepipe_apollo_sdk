from pydantic import BaseModel, Field
from .contact import Contact
from .organization import Organization


class People(BaseModel):
    contact: Contact = Field(default=None, alias='contact')
    organization: Organization = Field(default=None, alias='organization')
