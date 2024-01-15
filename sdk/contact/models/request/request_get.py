class RequestGet:
    def __init__(self, base_config: dict, name: str, email: str):
        self.__api_key = base_config['api_key']
        self.__url_base = base_config['url_base']
        self.__name = name
        self.__email = email

    @property
    def url(self) -> str:
        return f'{self.__url_base}/contacts/search'

    @property
    def header(self) -> dict[str: str]:
        return {
            'Cache-Control': 'no-cache'
        }

    @property
    def body(self) -> dict:
        return {
            'api_key': self.__api_key,
            'q_keywords': f'{self.__name}, {self.__email}'
        }
