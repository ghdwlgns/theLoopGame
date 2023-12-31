from objects.Object import Object

class Chest(Object):
    def __init__(self, x, y, image_uri, name, items):
        super().__init__(x, y, image_uri, name)
        self.inventory = items

    def interact(self, character, message_box):
        message_box.update_message("사용")

    def get_state(self):
        return {
            'name': self.name,
            'inventory': self.inventory
        }
    
    def load_state(self, state):
        self.name = state['name']
        self.inventory = state['inventory']
