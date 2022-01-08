"""
MiniMax Player with AlphaBeta pruning with heavy heuristic
"""
from players.AbstractPlayer import AbstractPlayer
import time
import utils
from SearchAlgos import AlphaBeta
import numpy as np


# TODO: you can import more modules, if needed


class Player(AbstractPlayer):
    def __init__(self, game_time):
        AbstractPlayer.__init__(self, game_time)  # keep the inheritance of the parent's (AbstractPlayer) __init__()
        self.is_game_started = False
        self.player = 0                             # At the beginning we don't know if we are player 1 or 2
        self.turn_num = 0
        self.state = utils.State(player=0,          # At the beginning we don't know if we are player 1 or 2
                                 board=np.full(24, 0),
                                 player_1_positions=np.full(9, -1),
                                 player_2_positions=np.full(9, -1),
                                 player_1_soldiers_num=0,
                                 player_2_soldiers_num=0,
                                 player_1_mills_num=0,
                                 player_2_mills_num=0,
                                 player_1_almost_mills_num=0,
                                 player_2_almost_mills_num=0)


    def set_game_params(self, board):
        """Set the game parameters needed for this player.
        This function is called before the game starts.
        (See GameWrapper.py for more info where it is called)
        input:
            - board: np.array, of the board.
        No output is expected.
        """
        self.state.board = board

    def make_move(self, time_limit):
        """Make move with this Player.
        input:
            - time_limit: float, time limit for a single turn.
        output:
            - direction: tuple, specifing the Player's movement
        """
        max_depth = 3
        end_time = time.time() + 99999999999999999
        if not self.is_game_started:
            self.player = 1
            self.state.player = 1
            self.turn_num = 1
            self.is_game_started = True
        curr_stage = 2 if self.turn_num > 18 else 1
        alphabeta = AlphaBeta(utils.utility, utils.succ, None, utils.is_goal, self.turn_num, self.player, end_time)
        best_succ = None
        max_val = float("-inf")
        alpha = utils.ALPHA_VALUE_INIT
        beta = utils.BETA_VALUE_INIT
        for next_succ in utils.succ(self.state, curr_stage):
            curr_val = alphabeta.search(next_succ, max_depth, False, 1, alpha, beta)
            if curr_val >= max_val:
                max_val = curr_val
                best_succ = next_succ
            if best_succ.is_winning_state(self.player, self.turn_num):
                break
            if max_val >= beta:
                break
            alpha = max(alpha, max_val)
        self.state = best_succ
        self.turn_num += 1
        return self.state.last_move

    def set_rival_move(self, move):
        """Update your info, given the new position of the rival.
        input:
            - move: tuple, the new position of the rival.
        No output is expected
        """
        if not self.is_game_started:
            self.player = 2
            self.state.player = 1
            self.turn_num = 2
            self.is_game_started = True
        else:
            self.turn_num += 1
        self.state.update_by_rival_move(move)
