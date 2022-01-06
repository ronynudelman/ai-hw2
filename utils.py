import operator
import numpy as np
import os

#TODO: edit the alpha and beta initialization values for AlphaBeta algorithm.
# instead of 'None', write the real initialization value, learned in class.
# hint: you can use np.inf
ALPHA_VALUE_INIT = None
BETA_VALUE_INIT = None


def get_possible_mills(position):
    mills = [
        [[1, 2], [3, 5]],    # 0
        [[0, 2], [9, 17]],   # 1
        [[0, 1], [4, 7]],    # 2
        [[11, 19], [0, 5]],  # 3
        [[12, 20], [2, 7]],  # 4
        [[6, 7], [0, 3]],    # 5
        [[5, 7], [14, 22]],  # 6
        [[5, 6], [2, 4]],    # 7
        [[9, 10], [11, 13]],  # 8
        [[8, 10], [1, 17]],  # 9
        [[8, 9], [12, 15]],  # 10
        [[3, 19], [8, 13]],  # 11
        [[4, 20], [10, 15]],  # 12
        [[14, 15], [8, 11]],  # 13
        [[13, 15], [6, 22]],  # 14
        [[13, 14], [10, 12]],  # 15
        [[17, 18], [19, 21]],  # 16
        [[16, 18], [1, 9]],  # 17
        [[16, 17], [20, 23]],  # 18
        [[3, 11], [16, 21]],  # 19
        [[4, 12], [18, 23]],  # 20
        [[22, 23], [16, 19]],  # 21
        [[21, 23], [6, 14]],  # 22
        [[21, 22], [18, 20]]  # 23
    ]
    return mills[position]


def get_directions(position):
    """Returns all the possible directions of a player in the game as a list.
    """
    assert 0 <= position <= 23, "illegal move"
    adjacent = [
        [1, 3],
        [0, 2, 9],
        [1, 4],
        [0, 5, 11],
        [2, 7, 12],
        [3, 6],
        [5, 7, 14],
        [4, 6],
        [9, 11],
        [1, 8, 10, 17],
        [9, 12],
        [3, 8, 13, 19],
        [4, 10, 15, 20],
        [11, 14],
        [6, 13, 15, 22],
        [12, 14],
        [17, 19],
        [9, 16, 18],
        [17, 20],
        [11, 16, 21],
        [12, 18, 23],
        [19, 22],
        [21, 23, 14],
        [20, 22]
    ]
    return adjacent[position]

# def tup_add(t1, t2):
#     """
#     returns the sum of two tuples as tuple.
#     """
#     return tuple(map(operator.add, t1, t2))


def printBoard(board):
    print(int(board[0]), "(00)-----------------------", int(board[1]),
          "(01)-----------------------", int(board[2]), "(02)")
    print("|                             |                             |")
    print("|                             |                             |")
    print("|                             |                             |")
    print("|       ", int(board[8]), "(08)--------------",
          int(board[9]), "(09)--------------", int(board[10]), "(10)   |")
    print("|       |                     |                    |        |")
    print("|       |                     |                    |        |")
    print("|       |                     |                    |        |")
    print("|       |        ", int(board[16]), "(16)-----", int(
        board[17]), "(17)-----", int(board[18]), "(18)   |        |")
    print("|       |         |                       |        |        |")
    print("|       |         |                       |        |        |")
    print("|       |         |                       |        |        |")
    print(int(board[3]), "(03)-", int(board[11]), "(11)---", int(board[19]), "(19)                 ",
          int(board[20]), "(20)-", int(board[12]), "(12)---", int(board[4]), "(04)")
    print("|       |         |                       |        |        |")
    print("|       |         |                       |        |        |")
    print("|       |         |                       |        |        |")
    print("|       |        ", int(board[21]), "(21)-----", int(
        board[22]), "(22)-----", int(board[23]), "(23)   |        |")
    print("|       |                     |                    |        |")
    print("|       |                     |                    |        |")
    print("|       |                     |                    |        |")
    print("|       ", int(board[13]), "(13)--------------",
          int(board[14]), "(14)--------------", int(board[15]), "(15)   |")
    print("|                             |                             |")
    print("|                             |                             |")
    print("|                             |                             |")
    print(int(board[5]), "(05)-----------------------", int(board[6]),
          "(06)-----------------------", int(board[7]), "(07)")
    print("\n")


def get_player_i_num_of_available_moves(player_i, board):
    counter = 0
    for pos, soldier in enumerate(board):
        if soldier == player_i:
            available_moves = get_directions(pos)
            for move in available_moves:
                if board[move] == 0:
                    counter += 1
    return counter


def is_player_i_can_move(player_i, board):
    for pos, soldier in enumerate(board):
        if soldier == player_i:
            available_moves = get_directions(pos)
            for move in available_moves:
                if board[move] == 0:
                    return True
    return False


def get_player_i_num_of_soldiers(player_i, board):
    return len(np.where(board == player_i))


def is_player_i_wins(player_i, board):
    if player_i == 1:
        if get_player_i_num_of_soldiers(player_i=2, board=board) < 3:
            return True
        if not is_player_i_can_move(player_i=2, board=board):
            return True
    else:
        if get_player_i_num_of_soldiers(player_i=1, board=board) < 3:
            return True
        if not is_player_i_can_move(player_i=1, board=board):
            return True
    return False


def check_goal(board):
    if is_player_i_wins(player_i=1, board=board):
        return 1
    if is_player_i_wins(player_i=2, board=board):
        return 2
    return 0


def is_goal(board):
    return check_goal(board) > 0


class State:

    def __init__(self, player_turn, board, player_1_positions, player_2_positions,
                 player_1_soldiers_num, player_2_soldiers_num,
                 player_1_mills_num, player_2_mills_num,
                 player_1_almost_mills_num, player_2_almost_mills_num):
        self.player_turn = player_turn
        self.board = board
        self.player_1_positions = player_1_positions
        self.player_2_positions = player_2_positions
        self.player_1_soldiers_num = player_1_soldiers_num
        self.player_2_soldiers_num = player_2_soldiers_num
        self.player_1_mills_num = player_1_mills_num
        self.player_2_mills_num = player_2_mills_num
        self.player_1_almost_mills_num = player_1_almost_mills_num
        self.player_2_almost_mills_num = player_2_almost_mills_num
        self.is_player_1_can_move = is_player_i_can_move(1, board)
        self.is_player_2_can_move = is_player_i_can_move(2, board)

    def print(self):
        print("self.player_turn =", self.player_turn)
        print("self.player_1_positions =", self.player_1_positions)
        print("self.player_2_positions =", self.player_2_positions)
        print("self.player_1_soldiers_num =", self.player_1_soldiers_num)
        print("self.player_2_soldiers_num =", self.player_2_soldiers_num)
        print("self.player_1_mills_num =", self.player_1_mills_num)
        print("self.player_2_mills_num =", self.player_2_mills_num)
        print("self.player_1_almost_mills_num =",
              self.player_1_almost_mills_num)
        print("self.player_2_almost_mills_num =",
              self.player_2_almost_mills_num)
        print("self.is_player_1_can_move =", self.is_player_1_can_move)
        print("self.is_player_2_can_move =", self.is_player_2_can_move)

    def is_goal(self):
        if self.player_1_soldiers_num < 3:
            return True
        if self.player_2_soldiers_num < 3:
            return True
        if not self.is_player_1_can_move:
            return True
        if not self.is_player_2_can_move:
            return True
        return False

    # update the board without removing the second player's soldier
    def stage_2_update_after_partial_move(self, player_i, prev_pos, next_pos,
                                          soldier_index):
        new_board = np.copy(self.board)
        new_board[next_pos] = player_i
        new_board[prev_pos] = 0
        new_player_1_positions = np.copy(self.player_1_positions)
        new_player_2_positions = np.copy(self.player_2_positions)
        if player_i == 1:
            new_player_1_positions[soldier_index] = next_pos
        else:
            new_player_2_positions[soldier_index] = next_pos
        return new_board, new_player_1_positions, new_player_2_positions

    def is_almost_mill(self, player_i, pos, board):
        new_almost_mill_counter = 0
        if board[pos] != 0 and board[pos] != player_i:
            return new_almost_mill_counter
        possible_mills = get_possible_mills(pos)
        horizontal_mill = possible_mills[0]
        vertical_mill = possible_mills[1]
        if board[pos] == 0:
            if board[horizontal_mill[0]] == player_i and board[horizontal_mill[1]] == player_i:
                new_almost_mill_counter += 1
            if board[vertical_mill[0]] == player_i and board[vertical_mill[1]] == player_i:
                new_almost_mill_counter += 1
        else:
            if board[horizontal_mill[0]] == player_i and board[horizontal_mill[1]] == 0:
                new_almost_mill_counter += 1
            if board[horizontal_mill[0]] == 0 and board[horizontal_mill[1]] == player_i:
                new_almost_mill_counter += 1
            if board[vertical_mill[0]] == player_i and board[vertical_mill[1]] == 0:
                new_almost_mill_counter += 1
            if board[vertical_mill[0]] == 0 and board[vertical_mill[1]] == player_i:
                new_almost_mill_counter += 1
        return new_almost_mill_counter

    def is_mill(self, player_i, pos, board):
        new_mill_counter = 0
        if board[pos] != player_i:
            return new_mill_counter
        possible_mills = get_possible_mills(pos)
        horizontal_mill = possible_mills[0]
        vertical_mill = possible_mills[1]
        if board[horizontal_mill[0]] == player_i and board[horizontal_mill[1]] == player_i:
            new_mill_counter += 1
        if board[vertical_mill[0]] == player_i and board[vertical_mill[1]] == player_i:
            new_mill_counter += 1
        return new_mill_counter

    def check_mill_was_created(self, player_i, pos, board,
                               mills_num, almost_mills_num):
        is_new_mill = False
        updated_mills_num = mills_num
        updated_almost_mills_num = almost_mills_num
        new_mill_counter = self.is_mill(player_i, pos, board)
        new_almost_mill_counter = self.is_almost_mill(player_i, pos, board)
        if new_mill_counter > 0:
            is_new_mill = True
            updated_mills_num = mills_num + new_mill_counter
            updated_almost_mills_num = almost_mills_num - new_mill_counter
        if new_almost_mill_counter > 0:
            updated_almost_mills_num += new_almost_mill_counter
        return is_new_mill, updated_mills_num, updated_almost_mills_num

    def check_mill_will_be_ruined(self, player_i, pos, board,
                                  mills_num, almost_mills_num):
        updated_mills_num = mills_num
        updated_almost_mills_num = almost_mills_num
        will_be_ruined_mill_counter = self.is_mill(player_i, pos, board)
        will_be_ruined_almost_mill_counter = self.is_almost_mill(player_i, pos, board)
        if will_be_ruined_mill_counter > 0:
            updated_mills_num = mills_num - will_be_ruined_mill_counter
            updated_almost_mills_num = almost_mills_num + will_be_ruined_mill_counter
        if will_be_ruined_almost_mill_counter > 0:
            updated_almost_mills_num -= will_be_ruined_almost_mill_counter
        return updated_mills_num, updated_almost_mills_num

    def update_after_soldier_killed(self, player_i, board, soldier_pos, soldier_index,
                                    player_1_positions, player_2_positions):
        new_board = np.copy(board)
        new_board[soldier_pos] = 0
        new_player_1_positions = np.copy(player_1_positions)
        new_player_2_positions = np.copy(player_2_positions)
        if player_i == 1:
            new_player_1_positions[soldier_index] = -2
        else:
            new_player_2_positions[soldier_index] = -2
        return new_board, new_player_1_positions, new_player_2_positions

    def stage_1_update_after_partial_move(self, player_i, pos):
        new_board = np.copy(self.board)
        new_player_1_positions = np.copy(self.player_1_positions)
        new_player_2_positions = np.copy(self.player_2_positions)
        new_board[pos] = player_i
        if player_i == 1:
            for index, soldier_position in enumerate(self.player_1_positions):
                if soldier_position == -1:
                    new_player_1_positions[index] = pos
                    break
        else:
            for index, soldier_position in enumerate(self.player_2_positions):
                if soldier_position == -1:
                    new_player_2_positions[index] = pos
                    break
        return new_board, new_player_1_positions, new_player_2_positions

    def stage_1_succ(self):
        if self.player_turn == 1:
            for pos, value in enumerate(self.board):
                if value == 0:
                    (before_insert_player_2_mills_num,
                     before_insert_player_2_almost_mills_num) = self.check_mill_will_be_ruined(2,
                                                                                               pos,
                                                                                               self.board,
                                                                                               self.player_2_mills_num,
                                                                                               self.player_2_almost_mills_num)
                    (after_insert_board,
                     after_insert_player_1_positions,
                     after_insert_player_2_positions) = self.stage_1_update_after_partial_move(1, pos)
                    (is_new_mill,
                     after_insert_player_1_mills_num,
                     after_insert_player_1_almost_mills_num) = self.check_mill_was_created(1,
                                                                                           pos,
                                                                                           after_insert_board,
                                                                                           self.player_1_mills_num,
                                                                                           self.player_1_almost_mills_num)
                    if is_new_mill:
                        for rival_index, rival_pos in enumerate(self.player_2_positions):
                            if rival_pos >= 0:
                                (after_kill_player_2_mills_num,
                                 after_kill_player_2_almost_mills_num) = self.check_mill_will_be_ruined(2,
                                                                                                        rival_pos,
                                                                                                        after_insert_board,
                                                                                                        before_insert_player_2_mills_num,
                                                                                                        before_insert_player_2_almost_mills_num)
                                (after_kill_board,
                                 after_kill_player_1_positions,
                                 after_kill_player_2_positions) = self.update_after_soldier_killed(2,
                                                                                                   after_insert_board,
                                                                                                   rival_pos,
                                                                                                   rival_index,
                                                                                                   after_insert_player_1_positions,
                                                                                                   after_insert_player_2_positions)
                                (_,
                                 after_kill_player_1_mills_num,
                                 after_kill_player_1_almost_mills_num) = self.check_mill_was_created(1,
                                                                                                     rival_pos,
                                                                                                     after_kill_board,
                                                                                                     after_insert_player_1_mills_num,
                                                                                                     after_insert_player_1_almost_mills_num)
                                yield State(2, after_kill_board,
                                            after_kill_player_1_positions, after_kill_player_2_positions,
                                            self.player_1_soldiers_num + 1, self.player_2_soldiers_num - 1,
                                            after_kill_player_1_mills_num, after_kill_player_2_mills_num,
                                            after_kill_player_1_almost_mills_num, after_kill_player_2_almost_mills_num)
                    else:
                        yield State(2, after_insert_board,
                                    after_insert_player_1_positions, after_insert_player_2_positions,
                                    self.player_1_soldiers_num + 1, self.player_2_soldiers_num,
                                    after_insert_player_1_mills_num, before_insert_player_2_mills_num,
                                    after_insert_player_1_almost_mills_num, before_insert_player_2_almost_mills_num)
        else:
            for pos, value in enumerate(self.board):
                if value == 0:
                    (before_insert_player_1_mills_num,
                     before_insert_player_1_almost_mills_num) = self.check_mill_will_be_ruined(1,
                                                                                               pos,
                                                                                               self.board,
                                                                                               self.player_1_mills_num,
                                                                                               self.player_1_almost_mills_num)
                    (after_insert_board,
                     after_insert_player_1_positions,
                     after_insert_player_2_positions) = self.stage_1_update_after_partial_move(2, pos)
                    (is_new_mill,
                     after_insert_player_2_mills_num,
                     after_insert_player_2_almost_mills_num) = self.check_mill_was_created(2,
                                                                                           pos,
                                                                                           after_insert_board,
                                                                                           self.player_2_mills_num,
                                                                                           self.player_2_almost_mills_num)
                    if is_new_mill:
                        for rival_index, rival_pos in enumerate(self.player_1_positions):
                            if rival_pos >= 0:
                                (after_kill_player_1_mills_num,
                                 after_kill_player_1_almost_mills_num) = self.check_mill_will_be_ruined(1,
                                                                                                        rival_pos,
                                                                                                        after_insert_board,
                                                                                                        before_insert_player_1_mills_num,
                                                                                                        before_insert_player_1_almost_mills_num)
                                (after_kill_board,
                                 after_kill_player_1_positions,
                                 after_kill_player_2_positions) = self.update_after_soldier_killed(1,
                                                                                                   after_insert_board,
                                                                                                   rival_pos,
                                                                                                   rival_index,
                                                                                                   after_insert_player_1_positions,
                                                                                                   after_insert_player_2_positions)
                                (_,
                                 after_kill_player_2_mills_num,
                                 after_kill_player_2_almost_mills_num) = self.check_mill_was_created(2,
                                                                                                     rival_pos,
                                                                                                     after_kill_board,
                                                                                                     after_insert_player_2_mills_num,
                                                                                                     after_insert_player_2_almost_mills_num)
                                yield State(1, after_kill_board,
                                            after_kill_player_1_positions, after_kill_player_2_positions,
                                            self.player_1_soldiers_num - 1, self.player_2_soldiers_num + 1,
                                            after_kill_player_1_mills_num, after_kill_player_2_mills_num,
                                            after_kill_player_1_almost_mills_num, after_kill_player_2_almost_mills_num)
                    else:
                        yield State(1, after_insert_board,
                                    after_insert_player_1_positions, after_insert_player_2_positions,
                                    self.player_1_soldiers_num, self.player_2_soldiers_num + 1,
                                    before_insert_player_1_mills_num, after_insert_player_2_mills_num,
                                    before_insert_player_1_almost_mills_num, after_insert_player_2_almost_mills_num)

    def stage_2_succ(self):
        if self.player_turn == 1:
            for soldier_index, prev_pos in enumerate(self.player_1_positions):
                if prev_pos >= 0:
                    (before_move_player_1_mills_num,
                     before_move_player_1_almost_mills_num) = self.check_mill_will_be_ruined(1,
                                                                                             prev_pos,
                                                                                             self.board,
                                                                                             self.player_1_mills_num,
                                                                                             self.player_1_almost_mills_num)
                    next_positions = get_directions(prev_pos)
                    for next_pos in next_positions:
                        if self.board[next_pos] == 0:
                            (after_move_board,
                             after_move_player_1_positions,
                             after_move_player_2_positions) = self.stage_2_update_after_partial_move(1,
                                                                                                     prev_pos,
                                                                                                     next_pos,
                                                                                                     soldier_index)
                            (is_new_mill,
                             after_move_player_1_mills_num,
                             after_move_player_1_almost_mills_num) = self.check_mill_was_created(1,
                                                                                                 next_pos,
                                                                                                 after_move_board,
                                                                                                 before_move_player_1_mills_num,
                                                                                                 before_move_player_1_almost_mills_num)
                            if is_new_mill:
                                for rival_index, rival_pos in enumerate(self.player_2_positions):
                                    if rival_pos >= 0:
                                        (after_kill_player_2_mills_num,
                                         after_kill_player_2_almost_mills_num) = self.check_mill_will_be_ruined(2,
                                                                                                                rival_pos,
                                                                                                                after_move_board,
                                                                                                                self.player_2_mills_num,
                                                                                                                self.player_2_almost_mills_num)
                                        (after_kill_board,
                                         after_kill_player_1_positions,
                                         after_kill_player_2_positions) = self.update_after_soldier_killed(2,
                                                                                                           after_move_board,
                                                                                                           rival_pos,
                                                                                                           rival_index,
                                                                                                           after_move_player_1_positions,
                                                                                                           after_move_player_2_positions)
                                        (_,
                                         after_kill_player_1_mills_num,
                                         after_kill_player_1_almost_mills_num) = self.check_mill_was_created(1,
                                                                                                             rival_pos,
                                                                                                             after_kill_board,
                                                                                                             after_move_player_1_mills_num,
                                                                                                             after_move_player_1_almost_mills_num)
                                        yield State(2, after_kill_board,
                                                    after_kill_player_1_positions, after_kill_player_2_positions,
                                                    self.player_1_soldiers_num, self.player_2_soldiers_num - 1,
                                                    after_kill_player_1_mills_num, after_kill_player_2_mills_num,
                                                    after_kill_player_1_almost_mills_num, after_kill_player_2_almost_mills_num)
                            else:
                                yield State(2, after_move_board,
                                            after_move_player_1_positions, after_move_player_2_positions,
                                            self.player_1_soldiers_num, self.player_2_soldiers_num,
                                            after_move_player_1_mills_num, self.player_2_mills_num,
                                            after_move_player_1_almost_mills_num, self.player_2_almost_mills_num)
        else:
            for soldier_index, prev_pos in enumerate(self.player_2_positions):
                if prev_pos >= 0:
                    (before_move_player_2_mills_num,
                     before_move_player_2_almost_mills_num) = self.check_mill_will_be_ruined(2,
                                                                                             prev_pos,
                                                                                             self.board,
                                                                                             self.player_2_mills_num,
                                                                                             self.player_2_almost_mills_num)
                    next_positions = get_directions(prev_pos)
                    for next_pos in next_positions:
                        if self.board[next_pos] == 0:
                            (after_move_board,
                             after_move_player_1_positions,
                             after_move_player_2_positions) = self.stage_2_update_after_partial_move(2,
                                                                                                     prev_pos,
                                                                                                     next_pos,
                                                                                                     soldier_index)
                            (is_new_mill,
                             after_move_player_2_mills_num,
                             after_move_player_2_almost_mills_num) = self.check_mill_was_created(2,
                                                                                                 next_pos,
                                                                                                 after_move_board,
                                                                                                 before_move_player_2_mills_num,
                                                                                                 before_move_player_2_almost_mills_num)
                            if is_new_mill:
                                for rival_index, rival_pos in enumerate(self.player_1_positions):
                                    if rival_pos >= 0:
                                        (after_kill_player_1_mills_num,
                                         after_kill_player_1_almost_mills_num) = self.check_mill_will_be_ruined(1,
                                                                                                                rival_pos,
                                                                                                                after_move_board,
                                                                                                                self.player_1_mills_num,
                                                                                                                self.player_1_almost_mills_num)
                                        (after_kill_board,
                                         after_kill_player_1_positions,
                                         after_kill_player_2_positions) = self.update_after_soldier_killed(1,
                                                                                                           after_move_board,
                                                                                                           rival_pos,
                                                                                                           rival_index,
                                                                                                           after_move_player_1_positions,
                                                                                                           after_move_player_2_positions)
                                        (_,
                                         after_kill_player_2_mills_num,
                                         after_kill_player_2_almost_mills_num) = self.check_mill_was_created(2,
                                                                                                             rival_pos,
                                                                                                             after_kill_board,
                                                                                                             after_move_player_2_mills_num,
                                                                                                             after_move_player_2_almost_mills_num)
                                        yield State(1, after_kill_board,
                                                    after_kill_player_1_positions, after_kill_player_2_positions,
                                                    self.player_1_soldiers_num - 1, self.player_2_soldiers_num,
                                                    after_kill_player_1_mills_num, after_kill_player_2_mills_num,
                                                    after_kill_player_1_almost_mills_num, after_kill_player_2_almost_mills_num)
                            else:
                                yield State(1, after_move_board,
                                            after_move_player_1_positions, after_move_player_2_positions,
                                            self.player_1_soldiers_num, self.player_2_soldiers_num,
                                            self.player_1_mills_num, after_move_player_2_mills_num,
                                            self.player_1_almost_mills_num, after_move_player_2_almost_mills_num)
