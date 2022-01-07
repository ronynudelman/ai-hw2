"""Search Algos: MiniMax, AlphaBeta
"""
#TODO: you can import more modules, if needed
#TODO: update ALPHA_VALUE_INIT, BETA_VALUE_INIT in utils
import time
import numpy as np
ALPHA_VALUE_INIT = -np.inf
BETA_VALUE_INIT = np.inf  # !!!!!


class SearchAlgos:
    def __init__(self, utility, succ, perform_move=None, goal=None, turn_num=None, player=0):
        """The constructor for all the search algos.
        You can code these functions as you like to, 
        and use them in MiniMax and AlphaBeta algos as learned in class
        :param utility: The utility function.
        :param succ: The succesor function.
        :param perform_move: The perform move function.
        :param goal: function that check if you are in a goal state.
        """
        self.utility = utility
        self.succ = succ
        self.perform_move = perform_move
        self.goal = goal
        self.turn_num = turn_num
        self.player = player

    def search(self, state, max_depth, maximizing_player, curr_depth):
        pass


class MiniMax(SearchAlgos):

    def search(self, state, max_depth, maximizing_player, curr_depth):
        """Start the MiniMax algorithm.
        :param state: The state to start from.
        :param max_depth: The maximum allowed depth for the algorithm.
        :param maximizing_player: Whether this is a max node (True) or a min node (False).
        :param curr_depth: The current depth
        :return: A tuple: (The min max algorithm value, The direction in case of max node or None in min mode)
        """
        curr_turn_num = self.turn_num + curr_depth
        curr_stage = 2 if curr_turn_num > 18 else 1
        if self.goal(state, curr_turn_num) or max_depth == curr_depth:
            return self.utility(state, self.player)
        if maximizing_player:
            max_val = float("-inf")
            for child in self.succ(state, curr_stage):
                max_val = max(max_val, self.search(child, max_depth, False, curr_depth + 1))
            return max_val
        else:
            min_val = float("inf")
            for child in self.succ(state, curr_stage):
                min_val = min(min_val, self.search(child, max_depth, True, curr_depth + 1))
            return min_val


class AlphaBeta(SearchAlgos):

    def search(self, state, depth, maximizing_player, alpha=ALPHA_VALUE_INIT, beta=BETA_VALUE_INIT):
        """Start the AlphaBeta algorithm.
        :param state: The state to start from.
        :param depth: The maximum allowed depth for the algorithm.
        :param maximizing_player: Whether this is a max node (True) or a min node (False).
        :param alpha: alpha value
        :param: beta: beta value
        :return: A tuple: (The min max algorithm value, The direction in case of max node or None in min mode)
        """
        #TODO: erase the following line and implement this function.
        raise NotImplementedError
