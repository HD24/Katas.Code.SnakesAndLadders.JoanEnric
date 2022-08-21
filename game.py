import random

from player import Player
from square import Square


class Game(object):
    """
    Main class, in this class we control everything about the game, players and board
    """

    def __init__(self, size_dice=6, size_board=100):
        assert type(size_board) is int
        self.__players = []
        self.__size_dice = size_dice
        self.__current_player = None
        self.__end_game = False

        self.__board = [None] * size_board

        # Initializing board and adding 1 to the value because index and position are different.
        # position 1 = index 0
        # ...
        # position 100 = index 99

        for square in range(size_board):
            self.__board[square] = Square(square + 1)

    @property
    def board(self):
        return self.__board

    @property
    def current_player(self):
        return self.__current_player

    @property
    def players(self):
        return self.__players

    @property
    def size_dice(self):
        return self.__size_dice

    @staticmethod
    def __check_menu_key(menu_key):
        try:
            if menu_key not in (["t", "T"]):
                raise ValueError
            return True
        except ValueError:
            print("Only the following options are accepted:")
            print("[T/t] to throw the dice")
            return False

    @staticmethod
    def __check_number_of_players(num_players):
        try:
            num_players = int(num_players)
            if num_players < 2:
                raise ValueError
            return True
        except ValueError:
            if type(num_players) is int:
                print("Number of players has to be greater than 2, currently is: " + str(num_players))
            else:
                print("Number of players has to be an integer greater than 2, currently is not and integer: " + str(num_players))
            return False

    def init_players_and_game(self, num_players):
        """
        This function create the players and choose the first player to start.
        :param num_players: Integer. Number of players to taking part.
        """
        assert type(num_players) is int
        for num_player in range(num_players):
            self.players.append(Player(num_player, 1))

        self.__current_player = random.choice(self.players)

    def move_token(self, n_positions):
        """
        This functions is used to move a player token and checks if the player has won the game.
        If the new position is bigger than the last position of the board, the player keeps in the same position.
        :param n_positions: Integer with the number of positions to moving.
        """
        assert type(n_positions) is int
        print("Player "+str(self.current_player.id)+" has to move "+str(n_positions)+" spaces.")
        new_token_position = self.current_player.token_position + n_positions

        # If the new position is bigger than the last position of the board, the player keeps in the same position.
        if new_token_position > self.board[-1].position:
            new_token_position = self.current_player.token_position

        self.current_player.token_position = new_token_position
        print("Player " + str(self.current_player.id) + " is on square " + str(self.current_player.token_position))

        # If the player's current position after moving, it's the last position of the board, the players win the game
        if self.current_player.token_position == self.board[-1].position:
            self.current_player.is_winner = True

    def player_rolls_a_dice(self):
        """
        This functions rolls the dice defined in the game
        :return:
        dice_value = Random integer between 1 and the size of the dice.
        """
        print("Player " + str(self.current_player.id) + " rolling a dice.")
        dice_value = random.choice(range(1, self.__size_dice+1))
        print("Player " + str(self.current_player.id) + " rolls a " + str(dice_value))
        return dice_value

    def player_plays(self):
        """
        Players rolling a dice and move token if is possible
        """
        dice_value = self.player_rolls_a_dice()
        self.move_token(dice_value)

    def config_game(self):
        """
        This function set up the players value and start the game
        """
        print("Welcome to a new game of Snake and Ladders!")

        str_num_players = input("Introduce how many players want to play:")
        while not Game.__check_number_of_players(str_num_players):
            str_num_players = input("Introduce how many players want to play:")

        print("There are: " + str_num_players + " players.")

        num_players = int(str_num_players)
        self.init_players_and_game(num_players)

        print("The players are:")
        for player in self.players:
            print("Player " + str(player.id))

        print("And starts the player: Player " + str(self.current_player.id))

    def play(self):
        """
        Main function. The current player rolls the dice until win.
        """
        self.config_game()

        while not self.__end_game:
            menu_key = input("If you want to roll the dice enter T or t and press Enter:")
            while not Game.__check_menu_key(menu_key):
                menu_key = input("If you want to roll the dice enter T or t and press Enter:")

            self.player_plays()

            if self.current_player.is_winner:
                print("Player " + str(self.current_player.id) + " is the winner!")
                print("Congratulations!")
                self.__end_game = True


if __name__ == '__main__':
    game = Game()
    game.play()




