from objects.Object import Object


class Door(Object):
    def __init__(self, x, y, sprite_uri, required_key, name):
        super().__init__(x, y, sprite_uri, name)
        self.required_key = required_key
        self.is_opened = False

    def interact(self, player, message_box):
        if not self.is_opened:
            if player.has_item(self.required_key):
                message_box.update("잠금을 해제했다.")
                self.is_opened = True
                player.remove_item(self.required_key)
            else:
                message_box.update("열쇠가 필요하다.")
        else:
            message_box.update("잠겨있다.")

    def draw(self, screen):
        if not self.is_opened:
            screen.blit(self.object_sprite_sheet, (self.x, self.y))


    def get_state(self):
        return {
            'name': self.name,
            'required_key': self.required_key,
            'is_opened': self.is_opened
        }
    
    def load_state(self, state):
        self.name = state['name']
        self.required_key = state['required_key']
        self.is_opened = state['is_opened']
