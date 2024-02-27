class RequestGet:
    def __init__(self, base_config: dict, web_domain: str):
        self.__api_key = base_config['api_key']
        self.__url_base = base_config['url_base']
        self.__web_domain = web_domain

    @property
    def url(self) -> str:
        return f'{self.__url_base}/organizations/enrich'

    @property
    def header(self) -> dict[str: str]:
        return {
            'Cache-Control': 'no-cache'
        }

    @property
    def body(self) -> dict:
        return {
            'api_key': self.__api_key,
            'domain': self.__web_domain
        }
