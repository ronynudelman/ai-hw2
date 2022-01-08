#!/usr/bin/env bash

touch results/minimax_alphabeta_move_time_20.txt
touch results/alphabeta_minimax_move_time_20.txt
touch results/minimax_alphabeta_move_time_60.txt
touch results/alphabeta_minimax_move_time_60.txt
touch results/compete_compete_game_time_2000.txt
touch results/global_global_game_time_2000.txt
touch results/minimax_simple_move_time_30.txt
touch results/simple_minimax_move_time_30.txt
touch results/alphabeta_simple_move_time_30.txt
touch results/simple_alphabeta_move_time_30.txt

echo 'Testing long tests...'

python3 main.py -player1 MinimaxPlayer -player2 AlphabetaPlayer -move_time 20 -game_time 10000 > results/minimax_alphabeta_move_time_20.txt
python3 main.py -player1 AlphabetaPlayer -player2 MinimaxPlayer -move_time 20 -game_time 10000 > results/alphabeta_minimax_move_time_20.txt
python3 main.py -player1 MinimaxPlayer -player2 AlphabetaPlayer -move_time 60 -game_time 10000 > results/minimax_alphabeta_move_time_60.txt
python3 main.py -player1 AlphabetaPlayer -player2 MinimaxPlayer -move_time 60 -game_time 10000 > results/alphabeta_minimax_move_time_60.txt
python3 main.py -player1 CompetePlayer -player2 CompetePlayer -move_time 2000 -game_time 2000 > results/compete_compete_game_time_2000.txt
python3 main.py -player1 GlobalTimeABPlayer -player2 GlobalTimeABPlayer -move_time 2000 -game_time 2000 > results/global_global_game_time_2000.txt
python3 main.py -player1 MinimaxPlayer -player2 SimplePlayer -move_time 30 > results/minimax_simple_move_time_30.txt
python3 main.py -player1 SimplePlayer -player2 MinimaxPlayer -move_time 30 > results/simple_minimax_move_time_30.txt
python3 main.py -player1 AlphabetaPlayer -player2 SimplePlayer -move_time 30 > results/alphabeta_simple_move_time_30.txt
python3 main.py -player1 SimplePlayer -player2 AlphabetaPlayer -move_time 30 > results/simple_alphabeta_move_time_30.txt

echo 'Done!'
