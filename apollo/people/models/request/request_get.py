class RequestGet:
    def __init__(
            self,
            base_config: dict,
            web_domain: str = None,
            first_name: str = None,
            last_name: str = None,
            email: str = None,
            linkedin_url: str = None,
            job_title: str = None,
            organization_name: str = None
    ):
        self.__api_key = base_config['api_key']
        self.__url_base = base_config['url_base']
        self.__web_domain = web_domain
        self.__first_name = first_name,
        self.__last_name = first_name,
        self.__last_name = last_name,
        self.__email = email
        self.__linkedin_url = linkedin_url,
        self.__job_title = job_title
        self.__organization_name = organization_name

    @property
    def url(self) -> str:
        return f'{self.__url_base}/people/match'

    @property
    def header(self) -> dict[str: str]:
        return {
            'Cache-Control': 'no-cache'
        }

    @property
    def body(self) -> dict:
        return {
            'api_key': self.__api_key,
            'domain': self.__web_domain,
            'first_name': self.__first_name,
            'last_name': self.__last_name,
            'email': self.__email,
            'linkedin_url': self.__linkedin_url,
            'title': self.__job_title,
            'organization_name': self.__organization_name
        }
