from .contact import ContactRequests
from .emailer_messages import EmailerMessagesRequests


class ApolloSdk:
    def __init__(self, api_key: str):
        self.__base_config = {
            'api_key': api_key,
            'url_base': 'https://api.apollo.io/v1/'
        }
        self.contact = ContactRequests(base_config=self.__base_config)
        self.emailer_messages = EmailerMessagesRequests(base_config=self.__base_config)
