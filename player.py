

class Player(object):

    def __init__(self, id_player, token_position):
        self.__id = id_player
        self.__token_position = token_position
        self.__is_winner = False

    @property
    def id(self):
        return self.__id

    @property
    def token_position(self):
        return self.__token_position

    @token_position.setter
    def token_position(self, new_token_position):
        self.__token_position = new_token_position

    @property
    def is_winner(self):
        return self.__is_winner

    @is_winner.setter
    def is_winner(self, player_is_winner):
        assert type(player_is_winner) is bool, "The value's type must to be a boolean"
        self.__is_winner = player_is_winner
