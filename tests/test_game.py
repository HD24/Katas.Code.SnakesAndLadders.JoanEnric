import unittest

from unittest import mock
from game import Game


class TestUS1(unittest.TestCase):
    """
    As a player
    I want to be able to move my token
    So that I can get closer to the goal
    """
    def setUp(self) -> None:
        self.num_player_for_test = 1

    def test_uat1(self):
        """
        Given the game is started
        When the token is placed on the board
        Then the token is on square 1
        """
        game = Game()
        game.init_players_and_game(self.num_player_for_test)

        for player in game.players:
            self.assertEqual(player.token_position, 1)  # add assertion here

    def test_uat2(self):
        """
        Given the token is on square 1
        When the token is moved 3 spaces
        Then the token is on square 4
        """
        game = Game()
        game.init_players_and_game(self.num_player_for_test)
        game.move_token(3)

        self.assertEqual(game.current_player.token_position, 4)

    def test_uat3(self):
        """
        Given the token is on square 1
        When the token is moved 3 spaces
        Then the token is on square 4
        """
        game = Game()
        game.init_players_and_game(self.num_player_for_test)
        game.move_token(3)
        game.move_token(4)

        self.assertEqual(game.current_player.token_position, 8)


class TestUS2(unittest.TestCase):
    """
    As a player
    I want to be able to win the game
    So that I can gloat to everyone around
    """
    def setUp(self) -> None:
        self.num_player_for_test = 1

    def test_uat1(self):
        """
        Given the token is on square 97
        When the token is moved 3 spaces
        Then the token is on square 100
        And the player has won the game
        """
        game = Game()
        game.init_players_and_game(self.num_player_for_test)
        game.current_player.token_position = 97
        game.move_token(3)

        self.assertEqual(game.current_player.is_winner, True)

    def test_uat2(self):
        """
        Given the token is on square 97
        When the token is moved 4 spaces
        Then the token is on square 97
        And the player has not won the game
        """
        game = Game()
        game.init_players_and_game(self.num_player_for_test)
        game.current_player.token_position = 97
        game.move_token(4)

        self.assertEqual(game.current_player.token_position, 97)
        self.assertEqual(game.current_player.is_winner, False)


class TestUS3(unittest.TestCase):
    """
    As a player
    I want to move my token based on the roll of a dice
    So that there is an element of chance in the game
    """
    def setUp(self) -> None:
        self.num_player_for_test = 1

    def test_uat1(self):
        """
        Given the game is started
        When the player rolls a dice
        Then the result should be between 1-6 inclusive
        """
        game = Game()
        game.init_players_and_game(self.num_player_for_test)
        dice_value = game.player_rolls_a_dice()

        self.assertIn(dice_value, range(1, 7))

    @mock.patch.object(Game, "player_rolls_a_dice")
    def test_uat2(self, mock_response):
        """
        Given the player rolls a 4
        When they move their token
        Then the token should move 4 spaces
        """
        game = Game()
        game.init_players_and_game(self.num_player_for_test)

        # Mocking response of rolling dice to 4
        mock_response.return_value = 4

        player_old_position = game.current_player.token_position
        game.player_plays()
        spaces_moved = game.current_player.token_position - player_old_position
        self.assertEqual(spaces_moved, 4)


if __name__ == '__main__':
    unittest.main()
