import unittest
import random
from reversi import Coord, Reversi
# from console1 import CLI


# This File Is For Unit Testing different components of the application

class CoordTest(unittest.TestCase):

    def setUp(self):
        self.upper = Coord(2, 5)
        self.lower = Coord(6, 0)

    def test_add_coordinates(self):
        coord = self.upper + self.lower
        self.assertEqual(coord.x, 8)
        self.assertEqual(coord.y, 5)

    def test_is_in_board(self):
        self.assertTrue(self.lower.is_in_board())
        self.assertFalse(Coord(8, 2).is_in_board())
        self.assertFalse(Coord(3, -1).is_in_board())


class ReversiInitialBoardTest(unittest.TestCase):

    def setUp(self):
        self.game = Reversi()

    def test_initial_board(self):
        self.assertEqual(len(self.game.board), 64)
        self.assertEqual(self.game.board[Coord(0, 1)], ' ')
        self.assertEqual(self.game.board[Coord(3, 4)], self.game.BLACK)

    def test_valid_move(self):
        self.assertTrue(self.game.is_valid_move(Coord(4, 5)))
        self.assertTrue(self.game.is_valid_move(Coord(3, 2)))
        self.assertFalse(self.game.is_valid_move(Coord(3, 1)))
        self.assertFalse(self.game.is_valid_move(Coord(3, 3)))

    def test_is_enemy_disc(self):
        self.assertTrue(self.game.is_enemy_disc(Coord(3, 3)))
        self.assertFalse(self.game.is_enemy_disc(Coord(7, 0)))
        self.assertFalse(self.game.is_enemy_disc(Coord(4, 3)))

    def test_play(self):
        self.game.play(Coord(4, 5))
        self.assertEqual(self.game.board[Coord(4, 4)], self.game.BLACK)
        self.assertEqual(self.game.board[Coord(4, 5)], self.game.BLACK)

    def test_available_fields(self):
        fields = {Coord(4, 5), Coord(5, 4), Coord(3, 2), Coord(2, 3)}
        self.assertEqual(fields, set(self.game.available_fields()))

    def test_outcome(self):
        self.assertEqual(
            self.game.outcome(), self.game.GAME_STATES['IN_PROGRESS'])

    def test_outcome_after_play(self):
        self.game.play(Coord(5, 4))
        self.assertEqual(
            self.game.outcome(), self.game.GAME_STATES['IN_PROGRESS'])

    def test_players_result(self):
        self.assertEqual(self.game.black_player.result, 2)
        self.assertEqual(self.game.white_player.result, 2)

    def test_change_current_player(self):
        self.game.change_current_player()
        self.assertEqual(self.game.player.field, self.game.WHITE)


class ReversiTest(unittest.TestCase):

    def setUp(self):
        # set board
        '''
        0   1   2   3   4   5   6   7
           │   │   │   │   │   │   │ O │0
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │   │   │ * │   │1
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │ O │   │   │ * │   │   │2
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │ * │ O │ * │   │   │   │3
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │ * │ O │   │   │   │4
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │ W │ * │ * │ O │   │   │5
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │ * │   │ * │   │   │   │   │6
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │ O │   │   │   │7
        ───┼───┼───┼───┼───┼───┼───┼───┼
        '''
        self.game = Reversi()
        self.game.board[Coord(0, 7)] = self.game.WHITE
        self.game.board[Coord(1, 6)] = self.game.BLACK
        self.game.board[Coord(2, 2)] = self.game.WHITE
        self.game.board[Coord(2, 5)] = self.game.BLACK

        self.game.board[Coord(3, 2)] = self.game.BLACK

        self.game.board[Coord(5, 3)] = self.game.BLACK
        self.game.board[Coord(5, 4)] = self.game.BLACK
        self.game.board[Coord(5, 5)] = self.game.WHITE

        self.game.board[Coord(6, 1)] = self.game.BLACK
        self.game.board[Coord(6, 3)] = self.game.BLACK
        self.game.board[Coord(7, 4)] = self.game.WHITE
        self.game.player = self.game.white_player

    def test_valid_move(self):
        self.assertTrue(self.game.is_valid_move(Coord(7, 3)))
        self.assertTrue(self.game.is_valid_move(Coord(4, 2)))
        self.assertTrue(self.game.is_valid_move(Coord(2, 4)))
        self.assertTrue(self.game.is_valid_move(Coord(6, 4)))
        self.assertTrue(self.game.is_valid_move(Coord(6, 2)))
        self.assertFalse(self.game.is_valid_move(Coord(6, 0)))

    def test_play_new_board(self):
        self.game.play(Coord(5, 2))
        # board after the turn
        '''
        0   1   2   3   4   5   6   7
           │   │   │   │   │   │   │ O │0
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │   │   │ O │   │1
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │ O │   │   │ O │   │   │2
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │ * │ O │ O │   │   │   │3
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │ O │ O │   │   │   │4
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │ O │ O │ O │ O │   │   │5
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │ * │   │ O │   │   │   │   │6
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │ O │   │   │   │7
        ───┼───┼───┼───┼───┼───┼───┼───┼
        '''
        new_board = self.game.board.copy()
        new_board[Coord(5, 2)] = self.game.WHITE
        new_board[Coord(1, 6)] = self.game.WHITE
        new_board[Coord(2, 5)] = self.game.WHITE
        new_board[Coord(4, 3)] = self.game.WHITE
        new_board[Coord(3, 4)] = self.game.WHITE
        new_board[Coord(6, 3)] = self.game.WHITE

        new_board[Coord(5, 3)] = self.game.WHITE
        new_board[Coord(5, 4)] = self.game.WHITE

        self.assertEqual(new_board, self.game.board)
        self.assertEqual(self.game.black_player.result, 2)
        self.assertEqual(self.game.white_player.result, 14)

    def test_available_fields(self):
        fields = {Coord(7, 3), Coord(4, 2), Coord(2, 4), Coord(6, 4),
                  Coord(6, 2), Coord(5, 2), Coord(3, 1), Coord(3, 5)}
        self.assertEqual(fields, set(self.game.available_fields()))

    def test_outcome(self):
        self.assertEqual(
            self.game.outcome(), self.game.GAME_STATES['IN_PROGRESS'])

    def test_outcome_after_play(self):
        self.game.play(Coord(2, 4))
        self.assertEqual(
            self.game.outcome(), self.game.GAME_STATES['IN_PROGRESS'])

    def black_player_discs_test(self):
        self.assertEqual(len(self.game.black_player_discs()), 9)

    def white_player_discs_test(self):
        self.assertEqual(len(self.game.white_player_discs()), 6)


class ReversiSkipTurn(unittest.TestCase):

    def setUp(self):
        # set board
        '''
        0   1   2   3   4   5   6   7
           │   │ O │ O │ O │   │   │ O │0
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │ * │   │   │   │   │1
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │   │   │   │   │2
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │   │   │   │   │3
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │   │   │   │   │4
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │   │   │   │   │5
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │   │   │   │   │6
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │   │   │ * │ * │7
        ───┼───┼───┼───┼───┼───┼───┼───┼
        '''
        self.game = Reversi()
        self.game.board[Coord(1, 3)] = self.game.BLACK
        self.game.board[Coord(0, 2)] = self.game.WHITE
        self.game.board[Coord(0, 3)] = self.game.WHITE
        self.game.board[Coord(0, 4)] = self.game.WHITE
        self.game.board[Coord(7, 7)] = self.game.BLACK
        self.game.board[Coord(7, 6)] = self.game.BLACK
        self.game.board[Coord(3, 3)] = self.game.EMPTY
        self.game.board[Coord(3, 4)] = self.game.EMPTY
        self.game.board[Coord(4, 3)] = self.game.EMPTY
        self.game.board[Coord(4, 4)] = self.game.EMPTY

    def test_outcome(self):
        self.assertEqual(
            self.game.outcome(), self.game.GAME_STATES['IN_PROGRESS'])

    def test_current_after_outcome(self):
        self.game.outcome()
        self.assertEqual(self.game.player.field, self.game.WHITE)


class ReversiEndGame(unittest.TestCase):

    def test_tie(self):
        # set board
        '''
        0   1   2   3   4   5   6   7
         O │ O │ O │ O │ O │ O │ O │ O │0
        ───┼───┼───┼───┼───┼───┼───┼───┼
         O │ O │ O │ O │ O │ O │ O │ O │1
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │   │   │   │   │2
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │   │   │   │   │3
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │   │   │   │   │4
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │   │   │   │   │5
        ───┼───┼───┼───┼───┼───┼───┼───┼
         * │ * │ * │ * │ * │ * │ * │ * │6
        ───┼───┼───┼───┼───┼───┼───┼───┼
         * │ * │ * │ * │ * │ * │ * │ * │7
        ───┼───┼───┼───┼───┼───┼───┼───┼
        '''
        self.game = Reversi()
        self.game.board[Coord(3, 3)] = self.game.EMPTY
        self.game.board[Coord(3, 4)] = self.game.EMPTY
        self.game.board[Coord(4, 3)] = self.game.EMPTY
        self.game.board[Coord(4, 4)] = self.game.EMPTY
        for row in range(2):
            for column in range(8):
                self.game.board[Coord(row, column)] = self.game.WHITE
        for row in range(6, 8):
            for column in range(8):
                self.game.board[Coord(row, column)] = self.game.BLACK
        self.assertEqual(self.game.outcome(), self.game.GAME_STATES['TIE'])

    def test_black_wins(self):
        # set board
        '''
        0   1   2   3   4   5   6   7
           │   │   │   │   │   │   │   │0
        ───┼───┼───┼───┼───┼───┼───┼───┼
         O │ O │ O │ O │ O │ O │ O │ O │1
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │   │   │   │   │2
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │   │   │   │   │3
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │   │   │   │   │4
        ───┼───┼───┼───┼───┼───┼───┼───┼
           │   │   │   │   │   │   │   │5
        ───┼───┼───┼───┼───┼───┼───┼───┼
         * │ * │ * │ * │ * │ * │ * │ * │6
        ───┼───┼───┼───┼───┼───┼───┼───┼
         * │ * │ * │ * │ * │ * │ * │ * │7
        ───┼───┼───┼───┼───┼───┼───┼───┼
        '''
        self.game = Reversi()
        self.game.board[Coord(3, 3)] = self.game.EMPTY
        self.game.board[Coord(3, 4)] = self.game.EMPTY
        self.game.board[Coord(4, 3)] = self.game.EMPTY
        self.game.board[Coord(4, 4)] = self.game.EMPTY
        for column in range(8):
            self.game.board[Coord(1, column)] = self.game.WHITE
        for row in range(6, 8):
            for column in range(8):
                self.game.board[Coord(row, column)] = self.game.BLACK
        self.game.black_player.result = len(self.game.black_player_discs())
        self.game.white_player.result = len(self.game.white_player_discs())
        self.assertEqual(
            self.game.outcome(), self.game.GAME_STATES["BLACK_WINS"])

    def test_white_wins(self):
        # set board
        '''
        0   1   2   3   4   5   6   7
         O │ O │ O │ O │ O │ O │ O │ O │0
        ───┼───┼───┼───┼───┼───┼───┼───┼
         * │ O │ O │ O │ O │ O │ O │ O │1
        ───┼───┼───┼───┼───┼───┼───┼───┼
         * │ * │ O │ O │ O │ O │ O │ O │2
        ───┼───┼───┼───┼───┼───┼───┼───┼
         * │ * │ * │ O │ O │ O │ O │ O │3
        ───┼───┼───┼───┼───┼───┼───┼───┼
         * │ * │ * │ * │ O │ O │ O │ O │4
        ───┼───┼───┼───┼───┼───┼───┼───┼
         * │ * │ * │ * │ * │ O │ O │ O │5
        ───┼───┼───┼───┼───┼───┼───┼───┼
         * │ * │ * │ * │ * │ * │ O │ O │6
        ───┼───┼───┼───┼───┼───┼───┼───┼
         * │ * │ * │ * │ * │ * │ * │ O │7
        ───┼───┼───┼───┼───┼───┼───┼───┼
        '''
        self.game = Reversi()
        for row in range(0, 8):
            for column in range(row, 8):
                self.game.board[Coord(row, column)] = self.game.WHITE
        for row in range(7, 0, -1):
            for column in range(row - 1, -1, -1):
                self.game.board[Coord(row, column)] = self.game.BLACK
        self.game.black_player.result = len(self.game.black_player_discs())
        self.game.white_player.result = len(self.game.white_player_discs())
        self.assertEqual(
            self.game.outcome(), self.game.GAME_STATES["WHITE_WINS"])


if __name__ == '__main__':
    unittest.main()
