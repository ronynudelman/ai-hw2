#!/usr/bin/env bash


echo 'python3 main.py -player1 MinimaxPlayer -player2 AlphabetaPlayer -move_time 120 -game_time 20000 > results/minimax_alphabeta_move_time_120.txt'
python3 main.py -player1 MinimaxPlayer -player2 AlphabetaPlayer -move_time 120 -game_time 10000 > results/minimax_alphabeta_move_time_120.txt

echo 'python3 main.py -player1 AlphabetaPlayer -player2 MinimaxPlayer -move_time 120 -game_time 20000 > results/alphabeta_minimax_move_time_120.txt'
python3 main.py -player1 AlphabetaPlayer -player2 MinimaxPlayer -move_time 120 -game_time 10000 > results/alphabeta_minimax_move_time_120.txt

echo 'python3 main.py -player1 MinimaxPlayer -player2 AlphabetaPlayer -move_time 300 -game_time 40000 > results/minimax_alphabeta_move_time_300.txt'
python3 main.py -player1 MinimaxPlayer -player2 AlphabetaPlayer -move_time 300 -game_time 10000 > results/minimax_alphabeta_move_time_300.txt

echo 'python3 main.py -player1 AlphabetaPlayer -player2 MinimaxPlayer -move_time 300 -game_time 40000 > results/alphabeta_minimax_move_time_300.txt'
python3 main.py -player1 AlphabetaPlayer -player2 MinimaxPlayer -move_time 300 -game_time 10000 > results/alphabeta_minimax_move_time_300.txt
