"""
MiniMax Player
"""
from players.AbstractPlayer import AbstractPlayer
#TODO: you can import more modules, if needed
import numpy as np
from SearchAlgos import MiniMax
import utils
import time


def is_enough_time(i):
    return i < 5


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
        self.state.board = board

    def make_move(self, time_limit):
        """Make move with this Player.
        input:
            - time_limit: float, time limit for a single turn.
        output:
            - direction: tuple, specifing the Player's movement
        """
        end_time = time.time() + time_limit
        if not self.is_game_started:
            self.player = 1
            self.state.player = 1
            self.turn_num = 1
            self.is_game_started = True
        curr_stage = 2 if self.turn_num > 18 else 1
        minimax = MiniMax(utils.utility, utils.succ, None, utils.is_goal, self.turn_num, self.player, end_time)
        best_succ = None
        max_depth = 1
        time_out = False
        while True:
            inner_max_val = float("-inf")
            inner_best_succ = None
            for next_succ in utils.succ(self.state, curr_stage):
                curr_val = minimax.search(next_succ, max_depth, False, 1)
                if curr_val is None:
                    time_out = True
                    break
                if curr_val >= inner_max_val:
                    inner_max_val = curr_val
                    inner_best_succ = next_succ
            if time_out:
                break
            best_succ = inner_best_succ
            max_depth += 1
        self.turn_num += 1
        if best_succ is not None:
            self.state = best_succ
        elif inner_best_succ is not None:
            self.state = inner_best_succ
        else:
            raise TimeoutError
        return self.state.last_move

    def set_rival_move(self, move):
        """Update your info, given the new position of the rival.
        input:
            - move: tuple, the new position of the rival.
        No output is expected
        """
        # TODO: erase the following line and implement this function.
        if not self.is_game_started:
            self.player = 2
            self.state.player = 1
            self.turn_num = 2
            self.is_game_started = True
        else:
            self.turn_num += 1
        self.state.update_by_rival_move(move)

    ########## helper functions in class ##########
    # TODO: add here helper functions in class, if needed



    ########## helper functions for AlphaBeta algorithm ##########
    # TODO: add here the utility, succ, an
