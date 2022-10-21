class CardCreator:
    def __init__(self, classname=None):
        self.process = classname

    def create_card(self, data, permissions, order, title):
        return self.process.create_card(self, data, permissions, order, title)



