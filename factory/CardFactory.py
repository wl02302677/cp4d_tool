from factory.CardCreator import CardCreator
from factory.ContentBlockCardCreator import ContentBlockCardCreator


class CardFactory:

    def init_card(self, class_name):
        card_creator = None
        if class_name == 'ContentBlockCardCreator':
            card_creator = CardCreator(ContentBlockCardCreator)

        return card_creator
