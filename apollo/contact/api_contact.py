import requests
from .models.response import ResponseContact
from .models.request import Get


class ApiContact:
    def __init__(self):
        pass

    def get(self, base_config: dict, name, email) -> ResponseContact:
        contact_get_model = Get(base_config=base_config, name=name, email=email)
        response = requests.post(
            url=contact_get_model.url,
            headers=contact_get_model.header,
            json=contact_get_model.body
        )
        if response.status_code == 429:
            raise Exception(f'Erro: {response.text}')
        return ResponseContact(**response.json())
