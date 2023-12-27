import requests
from .models.response import ResponseGet
from .models.request import RequestGet


class EmailerMessagesRequests:
    def __init__(self, base_config: dict) -> None:
        self.__base_config = base_config

    def get(self, status_email: str, opened_number: int, page: int) -> ResponseGet:
        get_model = RequestGet(
            base_config=self.__base_config,
            status_email=status_email,
            opened_number=opened_number,
            page=page
        )
        response = requests.post(
            url=get_model.url,
            headers=get_model.header,
            json=get_model.body
        )
        if response.status_code == 429:
            raise Exception(f'Erro: {response.text}')
        return ResponseGet(**response.json())
