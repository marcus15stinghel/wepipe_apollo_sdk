from src.wepipe_apollo_sdk.contact import ContactRequests
from src.wepipe_apollo_sdk.emailer_messages import EmailerMessagesRequests
from src.wepipe_apollo_sdk.enriched_organization import EnrichedOrganizationRequests
from src.wepipe_apollo_sdk.people import People


class WepipeApolloSdk:
    def __init__(self, api_key: str):
        self.__base_config = {
            'api_key': api_key,
            'url_base': 'https://api.apollo.io/v1/'
        }
        self.contact = ContactRequests(base_config=self.__base_config)
        self.emailer_messages = EmailerMessagesRequests(base_config=self.__base_config)
        self.enriched_organizations = EnrichedOrganizationRequests(base_config=self.__base_config)
        self.people = People(base_config=self.__base_config)
