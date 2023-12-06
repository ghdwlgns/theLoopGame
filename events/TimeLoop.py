class TimeLoop:
    @staticmethod
    def save_state(player, objects):
        if objects is None:
            objects = []
        state = {
            'player': {
                'position': (player.x, player.y)
            },
            'objects': [{'name': obj.name, 'position': (obj.x, obj.y)} for obj in objects]
        }

        return state

    @staticmethod
    def load_state(player, objects, state, ):
        player.x, player.y = state['player']['position']

        for obj, obj_state in zip(objects, state['objects']):
            obj.x, obj.y = obj_state['position']
