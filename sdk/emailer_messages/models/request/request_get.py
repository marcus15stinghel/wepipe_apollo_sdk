class RequestGet:
    def __init__(self, base_config: dict, status_email: str, opened_number: int, page: int):
        self.__api_key = base_config['api_key']
        self.__url_base = base_config['url_base']
        self.__status_email = status_email
        self.__opened_number = str(opened_number)
        self.__page = page

    @property
    def url(self) -> str:
        return f'{self.__url_base}/emailer_messages/search'

    @property
    def header(self) -> dict[str: str]:
        return {
            'Cache-Control': 'no-cache'
        }

    @property
    def body(self) -> dict:
        return {
            'api_key': self.__api_key,
            'num_emailer_message_opens_at_least': self.__opened_number,
            'emailer_message_stats': self.__status_email,
            'page': self.__page
        }
