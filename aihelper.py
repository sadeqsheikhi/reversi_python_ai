from reversi import Coord, Reversi, Player
from collections import OrderedDict

class AIHelper():
    MAX_PLAYER = 'w'
    MIN_PLAYER = 'b'
    INFINITY = 1.0e+10

    """
    Helper interface class for the AI
        $1. available moves (board, player)
        $2. get_resulting_board -> (board, player, coord)
        $3. player pools (board, player)
        $4. check if game has ended (board)
    """

    # it is created when the game starts
    def __init__(self, board=None):
        self.game = Reversi()
        if board:
            self.set_board(board)

    # changes to board form ai to game board
    def set_board(self, board):
        self.game.board = FormatConverter.ai_to_game_board(board)

    # sets a player
    def set_player(self, player):
        self.game.player = Player(player)

    # finding available moves
    def available_moves(self, board, player):
        self.set_board(board)
        self.set_player(player)
        return self.game.available_fields()

    # gets the changes of the human player
    def get_resulting_board(self, board, player, coord):
        self.set_board(board)
        self.set_player(player)
        self.game.play(coord)
        return FormatConverter.game_to_ai_board(self.game.board)


    def player_pool(self, board, player):
        self.set_board(board)
        # probably this is an error
        return ''.join(''.join(row) for row in self.board).count(player)

    # defines if the game is over or not
    def is_game_over(self, board):
        self.set_board(board)
        return self.game.outcome() != self.game.GAME_STATES["IN_PROGRESS"]


class FormatConverter():

    @staticmethod
    def ai_to_game_board(ai_board):
        return OrderedDict((Coord(i, j), ai_board[i][j])
                           for i in range(8) for j in range(8))

    @staticmethod
    def game_to_ai_board(game_board):
        return [[game_board[Coord(i, j)] for j in range(8)] for i in range(8)]
