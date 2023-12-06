from objects.Object import Object


class Door(Object):
    def __init__(self, x, y, width, height, sprite_uri, required_key):
        super().__init__(x, y, width, height, sprite_uri)
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
