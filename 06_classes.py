from abc import ABC


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
        print(f'Playing game {game_name}')

    @classmethod
    def demonstrate_classmethod(cls):
        print("I'm a classmethod")

    @classmethod
    def play_game_class(cls, game_name):
        cls.demonstrate_classmethod()
        print(f'Playing game {game_name}')

    @staticmethod
    def play_game_static(game_name):
        print(f'Playing game {game_name}')


phone_1 = Phone('Nokia')
phone_2 = Phone('Siemens')
gaming_phone = GamingPhone('Sony', 'Game')

gaming_phone.play_game('cyberpunk 2077')
GamingPhone.play_game_class('cyberpunk 2078')
GamingPhone.play_game_static('cyberpunk 2079')


def function(parameter_list):
    return parameter_list
