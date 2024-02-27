from pydantic import BaseModel, Field
from typing import List
from .emailer_messages import EmailerMessages


class ResponseGet(BaseModel):
    data: List[EmailerMessages] = Field(default=None, alias='emailer_messages')
