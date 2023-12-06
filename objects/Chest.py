from objects.Object import Object


class Chest(Object):
    def __init__(self, x, y, image_uri, name, items):
        super().__init__(x, y, image_uri, name)
        self.inventory = items

    def interact(self, character, message_box):
        print("사용")