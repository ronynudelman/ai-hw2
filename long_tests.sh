#!/usr/bin/env bash

echo 'Testing long tests...'

echo '0'
python3 main.py -player1 MinimaxPlayer -player2 AlphabetaPlayer -move_time 20 -game_time 5000 > results/minimax_alphabeta_move_time_20.txt
echo '1'
python3 main.py -player1 AlphabetaPlayer -player2 MinimaxPlayer -move_time 20 -game_time 5000 > results/alphabeta_minimax_move_time_20.txt
echo '2'
python3 main.py -player1 MinimaxPlayer -player2 AlphabetaPlayer -move_time 60 -game_time 5000 > results/minimax_alphabeta_move_time_60.txt
echo '3'
python3 main.py -player1 AlphabetaPlayer -player2 MinimaxPlayer -move_time 60 -game_time 5000 > results/alphabeta_minimax_move_time_60.txt
echo '4'
python3 main.py -player1 CompetePlayer -player2 CompetePlayer -move_time 2000 -game_time 2000 > results/compete_compete_game_time_2000.txt
echo '5'
python3 main.py -player1 GlobalTimeABPlayer -player2 GlobalTimeABPlayer -move_time 2000 -game_time 2000 > results/global_global_game_time_2000.txt
echo '6'
python3 main.py -player1 MinimaxPlayer -player2 SimplePlayer -move_time 30 > results/minimax_simple_move_time_30.txt
echo '7'
python3 main.py -player1 SimplePlayer -player2 MinimaxPlayer -move_time 30 > results/simple_minimax_move_time_30.txt
echo '8'
python3 main.py -player1 AlphabetaPlayer -player2 SimplePlayer -move_time 30 > results/alphabeta_simple_move_time_30.txt
echo '9'
python3 main.py -player1 SimplePlayer -player2 AlphabetaPlayer -move_time 30 > results/simple_alphabeta_move_time_30.txt

echo 'Done!'
