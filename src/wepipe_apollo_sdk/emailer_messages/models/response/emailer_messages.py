from pydantic import BaseModel, Field
from typing import List
from .data_people import DataPeople


class EmailerMessages(BaseModel):
    data_people: List[DataPeople] = Field(default=None, alias='recipients')
    num_clicks: int = Field(default=None)
