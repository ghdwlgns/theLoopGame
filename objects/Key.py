from objects.Item import Item


class Key(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def use(self, message_box):
        message_box.update("열쇠를 사용했다.")