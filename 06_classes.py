class Phone:
    def __init__(self, model):
        self.model = model

    def call(self, number):
        print(f'Calling number: {number}')


class GamingPhone(Phone):
    def __init__(self, model, default_game):
        super().__init__(model)
        self.default_game = default_game

    def play_game(self, game_name):
        print(f'Playing game{game_name}')


phone_1 = Phone('Nokia')
phone_2 = Phone('Siemens')
gaming_phone = GamingPhone('Sony', 'Game')
