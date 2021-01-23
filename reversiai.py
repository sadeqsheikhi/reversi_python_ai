from aihelper import AIHelper


class ReversiAI():

    # runs the minimax with precision
    @staticmethod
    def get_next_move(board, player):
        # the depth argument defines how many levels deep we go before using heuristic
        _, move = ReversiAI.minimax(board, 2, player)
        return move

    @staticmethod
    def minimax(board, depth, player):
        helper = AIHelper()

        # if game is over then return something
        if helper.is_game_over(board) or depth == 0:
            return (ReversiAI.game_heuristic(board), None)

        best_move = None
        # if it is a max node
        if player == AIHelper.MAX_PLAYER:
            best_value = -AIHelper.INFINITY
            available_moves = helper.available_moves(
                board, AIHelper.MAX_PLAYER)
            for move in available_moves:
                node = helper.get_resulting_board(
                    board, AIHelper.MAX_PLAYER, move)
                value, _ = ReversiAI.minimax(
                    node, depth - 1, AIHelper.MIN_PLAYER)
                if value > best_value:
                    best_value = value
                    best_move = move
            return (best_value, best_move)

        # if it is a min node
        else:
            best_value = AIHelper.INFINITY
            available_moves = helper.available_moves(
                board, AIHelper.MIN_PLAYER)
            for move in available_moves:
                node = helper.get_resulting_board(
                    board, AIHelper.MIN_PLAYER, move)
                value, _ = ReversiAI.minimax(
                    node, depth - 1, AIHelper.MAX_PLAYER)
                if value < best_value:
                    best_value = value
                    best_move = move
            return (best_value, best_move)

    @staticmethod
    def game_heuristic(board):
        # defining the ai and Opponent color
        my_color = AIHelper.MAX_PLAYER
        opp_color = AIHelper.MIN_PLAYER

        my_tiles = 0
        opp_tiles = 0
        my_front_tiles = 0
        opp_front_tiles = 0

        p = 0
        c = 0
        l = 0
        m = 0
        f = 0
        d = 0

        # these two are used for going in every 8 directions
        X1 = [-1, -1, 0, 1, 1, 1, 0, -1]
        Y1 = [0, 1, 1, 1, 0, -1, -1, -1]

        # wondering where this came from? check the link in the github ripo from University of Washington
        V = [
            [20, -3, 11, 8, 8, 11, -3, 20],
            [-3, -7, -4, 1, 1, -4, -7, -3],
            [11, -4, 2, 2, 2, 2, -4, 11],
            [8, 1, 2, -3, -3, 2, 1, 8],
            [8, 1, 2, -3, -3, 2, 1, 8],
            [11, -4, 2, 2, 2, 2, -4, 11],
            [-3, -7, -4, 1, 1, -4, -7, -3],
            [20, -3, 11, 8, 8, 11, -3, 20]
        ]

        # =============================================================================================
        # 1- Piece difference, frontier disks and disk squares
        # =============================================================================================
        for i in range(8):
            for j in range(8):
                if board[i][j] == my_color:
                    d += V[i][j]
                    my_tiles += 1
                elif board[i][j] == opp_color:
                    d -= V[i][j]
                    opp_tiles += 1

                # calculates the number of blank spaces around me
                # if the tile is not empty take a step in each direction
                if board[i][j] != ' ':
                    for k in range(8):
                        x = i + X1[k]
                        y = j + Y1[k]
                        if (x >= 0 and x < 8 and y >= 0 and y < 8 and
                                board[x][y] == ' '):
                            if board[i][j] == my_color:
                                my_front_tiles += 1
                            else:
                                opp_front_tiles += 1
                            break

        # =============================================================================================
        # 2 - calculates the difference between current colored tiles
        # =============================================================================================
        if my_tiles > opp_tiles:
            p = (100.0 * my_tiles) / (my_tiles + opp_tiles)
        elif my_tiles < opp_tiles:
            p = -(100.0 * opp_tiles) / (my_tiles + opp_tiles)
        else:
            p = 0

        # =============================================================================================
        # 3- calculates the blank Spaces around my tiles
        # =============================================================================================
        if my_front_tiles > opp_front_tiles:
            f = -(100.0 * my_front_tiles) / (my_front_tiles + opp_front_tiles)
        elif my_front_tiles < opp_front_tiles:
            f = (100.0 * opp_front_tiles) / (my_front_tiles + opp_front_tiles)
        else:
            f = 0

        # ===============================================================================================
        # 4 - Corner occupancy
        '''
        Examine all 4 corners :
        if they were my color add a point to me 
        if they were enemies add a point to the enemy
        '''
        # ===============================================================================================
        my_tiles = opp_tiles = 0
        if board[0][0] == my_color:
            my_tiles += 1
        elif board[0][0] == opp_color:
            opp_tiles += 1
        if board[0][7] == my_color:
            my_tiles += 1
        elif board[0][7] == opp_color:
            opp_tiles += 1
        if board[7][0] == my_color:
            my_tiles += 1
        elif board[7][0] == opp_color:
            opp_tiles += 1
        if board[7][7] == my_color:
            my_tiles += 1
        elif board[7][7] == opp_color:
            opp_tiles += 1
        c = 25 * (my_tiles - opp_tiles)

        # ===============================================================================================
        # 5 - CORNER CLOSENESS
        '''
        If the corner is empty then find out how many of the 
        adjacent block to the corner are AI's or the player's
        if AI's tiles were mote than players than it's a bad thing.
        '''
        # ===============================================================================================
        my_tiles = opp_tiles = 0
        if board[0][0] == ' ':
            if board[0][1] == my_color:
                my_tiles += 1
            elif board[0][1] == opp_color:
                opp_tiles += 1
            if board[1][1] == my_color:
                my_tiles += 1
            elif board[1][1] == opp_color:
                opp_tiles += 1
            if board[1][0] == my_color:
                my_tiles += 1
            elif board[1][0] == opp_color:
                opp_tiles += 1

        if board[0][7] == ' ':
            if board[0][6] == my_color:
                my_tiles += 1
            elif board[0][6] == opp_color:
                opp_tiles += 1
            if board[1][6] == my_color:
                my_tiles += 1
            elif board[1][6] == opp_color:
                opp_tiles += 1
            if board[1][7] == my_color:
                my_tiles += 1
            elif board[1][7] == opp_color:
                opp_tiles += 1

        if board[7][0] == ' ':
            if board[7][1] == my_color:
                my_tiles += 1
            elif board[7][1] == opp_color:
                opp_tiles += 1
            if board[6][1] == my_color:
                my_tiles += 1
            elif board[6][1] == opp_color:
                opp_tiles += 1
            if board[6][0] == my_color:
                my_tiles += 1
            elif board[6][0] == opp_color:
                opp_tiles += 1

        if board[7][7] == ' ':
            if board[6][7] == my_color:
                my_tiles += 1
            elif board[6][7] == opp_color:
                opp_tiles += 1
            if board[6][6] == my_color:
                my_tiles += 1
            elif board[6][6] == opp_color:
                opp_tiles += 1
            if board[7][6] == my_color:
                my_tiles += 1
            elif board[7][6] == opp_color:
                opp_tiles += 1

        l = -12.5 * (my_tiles - opp_tiles)

        # ===============================================================================================
        # 6 - Mobility
        # ===============================================================================================
        '''
        It attempts to capture the relative difference between 
        the number of possible moves for the max and the min players,
        with the intent of restricting the
        opponent’s mobility and increasing one’s own mobility
        '''
        # basically it calculates the difference between available moves
        my_tiles = len(AIHelper().available_moves(board, AIHelper.MAX_PLAYER))
        opp_tiles = len(AIHelper().available_moves(board, AIHelper.MIN_PLAYER))

        if my_tiles > opp_tiles:
            m = (100.0 * my_tiles) / (my_tiles + opp_tiles)
        elif my_tiles < opp_tiles:
            m = -(100.0 * opp_tiles) / (my_tiles + opp_tiles)
        else:
            m = 0

        # =============================================================================================
        # =============================================================================================
        # final weighted score
        # adding different weights to different evaluations
        return (10 * p) + (801.724 * c) + (382.026 * l) + \
               (78.922 * m) + (74.396 * f) + (10 * d)
