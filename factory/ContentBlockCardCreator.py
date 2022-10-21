from model.Card import Card


class ContentBlockCardCreator:

    def create_card(self, data, permissions, order, title):
        card = Card()
        card.set_template_type('content_block')
        card.set_data(data)
        card.set_order(order)
        card.set_title(title)
        card.set_permissions(permissions)

        return card


if __name__ == '__main__':
    test = ContentBlockCardCreator()
