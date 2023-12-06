from objects.Item import Item


class TimeLoop:
    @staticmethod
    def save_state(player, objects):
        state = {
            'player': {
                'position': (player.character_x, player.character_y)
            },
            'objects': [{'name': obj.name, 'position': (obj.x, obj.y)} for obj in objects]
        }

        return state

    @staticmethod
    def load_state(player, objects, state):
        player.inventory = [Item(name, '') for name in state['player']['inventory']]
        player.character_x, player.character_y = state['player']['position']

        for obj, obj_state in zip(objects, state['objects']):
            obj.x, obj.y = obj_state['position']
