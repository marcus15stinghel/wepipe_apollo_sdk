import requests
from .models.response import ResponseGet
from .models.request import RequestGet


class EnrichedOrganizationRequests:
    def __init__(self, base_config: dict) -> None:
        self.__base_config = base_config

    def get(self, web_domain: str) -> ResponseGet:
        get_model = RequestGet(
            base_config=self.__base_config,
            web_domain=web_domain
        )
        response = requests.post(
            url=get_model.url,
            headers=get_model.header,
            json=get_model.body
        )
        if response.status_code == 429:
            raise Exception(f'Erro: {response.text}')
        return ResponseGet(**response.json())
