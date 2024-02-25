import requests
from .models.response import ResponseGet
from .models.request import RequestGet


class People:
    def __init__(self, base_config: dict) -> None:
        self.__base_config = base_config

    def get(
            self,
            web_domain: str = None,
            first_name: str = None,
            last_name: str = None,
            email: str = None,
            linkedin_url: str = None,
            job_title: str = None,
            organization_name: str = None
    ) -> ResponseGet:
        get_model = RequestGet(
            base_config=self.__base_config,
            web_domain=web_domain,
            first_name=first_name,
            last_name=last_name,
            email=email,
            linkedin_url=linkedin_url,
            job_title=job_title,
            organization_name=organization_name
        )
        response = requests.post(
            url=get_model.url,
            headers=get_model.header,
            json=get_model.body
        )
        if response.status_code == 429:
            raise Exception(f'Erro: {response.text}')
        return ResponseGet(**response.json())
