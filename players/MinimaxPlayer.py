"""
MiniMax Player
"""
from players.AbstractPlayer import AbstractPlayer
#TODO: you can import more modules, if needed
import numpy as np
from SearchAlgos import MiniMax

class Player(AbstractPlayer):
    def __init__(self, game_time):
        AbstractPlayer.__init__(self, game_time) # keep the inheritance of the parent's (AbstractPlayer) __init__()
        #TODO: initialize more fields, if needed, and the AlphaBeta algorithm from SearchAlgos.py

    def set_game_params(self, board):
        """Set the game parameters needed for this player.
        This function is called before the game starts.
        (See GameWrapper.py for more info where it is called)
        input:
            - board: np.array, of the board.
        No output is expected.
        """
        # TODO: erase the following line and implement this function.
        self.board = board

    def make_move(self, time_limit):
        """Make move with this Player.
        input:
            - time_limit: float, time limit for a single turn.
        output:
            - direction: tuple, specifing the Player's movement
        """
        #TODO: erase the following line and implement this function.
        minimax = MiniMax(utility, succ, None, AbstractPlayer.is_goal, self.turn_num)
        depth = 1
        best_succ = None
        while self.is_enough_time():
            max_val = float("-inf")
            max_next_succ = None
            for next_succ in succ(self.board):
                curr_val = minimax.search(next_succ, depth-1, False)
                if curr_val > max_val:
                    max_next_succ = next_succ
                    max_val = curr_val
            best_succ = max_next_succ
        next_player_pos, number_of_soldier, rival_dead_pos = self.parse_succ_to_direction(best_next_succ)
        self.update_player_after_move(best_succ, number_of_soldier, next_player_pos, rival_dead_pos)
        return next_player_pos, number_of_soldier, rival_dead_pos

    def update_player_after_move(self, succ, number_of_soldier, next_player_pos, rival_dead_pos):
        self.player_positions[number_of_soldier] = next_player_pos
        rival_dead_soldier = np.where(self.rival_positions == rival_dead_pos)[0]
        self.rival_positions[rival_dead_soldier] = -2
        self.board = succ
        self.turn_num += 1

    @staticmethod
    def get_rival_dead_pos(diff):
        rival_dead_pos = np.where(diff == 2)
        if len(rival_dead_pos) == 0:
            rival_dead_pos = -1
        else:
            rival_dead_pos = rival_dead_pos[0]
        return rival_dead_pos

    @staticmethod
    def get_next_player_pos(diff):
        return np.where(diff == -1)[0]

    def get_number_of_soldier(self, diff, next_player_pos):
        prev_player_pos = np.where(diff == 1)
        if len(prev_player_pos) == 0:
            number_of_soldier = np.where(self.player_positions == -1)[0]
        else:
            number_of_soldier = np.where(self.player_positions == prev_player_pos[0])[0]
        return number_of_soldier

    def parse_succ_to_direction(self, succ):
        diff = self.board - succ
        rival_dead_pos = self.get_rival_dead_pos(diff)
        next_player_pos = self.get_next_player_pos(diff)
        number_of_soldier = self.get_number_of_soldier(diff, next_player_pos)
        return next_player_pos, number_of_soldier, rival_dead_pos

    def set_rival_move(self, move):
        """Update your info, given the new position of the rival.
        input:
            - move: tuple, the new position of the rival.
        No output is expected
        """
        # TODO: erase the following line and implement this function.
        raise NotImplementedError



    ########## helper functions in class ##########
    # TODO: add here helper functions in class, if needed



    ########## helper functions for AlphaBeta algorithm ##########
    # TODO: add here the utility, succ, an
