class Card:

    def __init__(self):
        self.data = None
        self.permissions = None
        self.order = None
        self.title = None
        self.template_type = None

    def set_data(self, data):
        self.data = data

    def set_permissions(self, permissions: list):
        self.permissions = permissions

    def set_order(self, order: int):
        self.order = order

    def set_title(self, title: str):
        self.title = title

    def set_template_type(self, template_type: str):
        self.template_type = template_type

