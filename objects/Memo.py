from objects.Item import Item


class Memo(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def use(self, message_box):
        message_box.update(self.description)