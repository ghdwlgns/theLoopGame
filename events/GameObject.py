import pickle

class GameObject:
    def save_game_state(self, player, objects, file="save_game.txt"):
        game_state = {
            'player': player.get_state(),
            'objects': [obj.get_state() for obj in objects]
        }

        with open(file, 'wb') as file:
            pickle.dump(game_state, file)

    def load_game_state(self, file="save_game.txt"):
        try:
            with open(file, 'rb') as file:
                game_state = pickle.load(file)

            return game_state

        except FileNotFoundError:
            print("Save file not found. Starting a new game.")
        except Exception as e:
            print(f"Error loading game state: {e}")