#!/usr/bin/env bash

echo 'Testing minimax vs. alphabeta'
python3 main.py -player1 MinimaxPlayer -player2 AlphabetaPlayer -move_time 5 > results/minimax_alphabeta_move_time_5.txt
python3 main.py -player1 AlphabetaPlayer -player2 MinimaxPlayer -move_time 5 > results/alphabeta_minimax_move_time_5.txt
python3 main.py -player1 MinimaxPlayer -player2 AlphabetaPlayer -move_time 10 > results/minimax_alphabeta_move_time_10.txt
python3 main.py -player1 AlphabetaPlayer -player2 MinimaxPlayer -move_time 10 > results/alphabeta_minimax_move_time_10.txt

# echo 'Testing heavy vs. light'
# python3 main.py -player1 LightABPlayer -player2 HeavyABPlayer -move_time 2000 -game_time 2000 > results/light_heavy.txt
# python3 main.py -player1 HeavyABPlayer -player2 LightABPlayer -move_time 2000 -game_time 2000 > results/heavy_light.txt

echo 'Testing compete vs. compete'
python3 main.py -player1 CompetePlayer -player2 CompetePlayer -move_time 100 -game_time 100 > results/compete_compete_game_time_100.txt
python3 main.py -player1 CompetePlayer -player2 CompetePlayer -move_time 200 -game_time 200 > results/compete_compete_game_time_200.txt
python3 main.py -player1 CompetePlayer -player2 CompetePlayer -move_time 500 -game_time 500 > results/compete_compete_game_time_500.txt

echo 'Testing global_time vs. global_time'
python3 main.py -player1 GlobalTimeABPlayer -player2 GlobalTimeABPlayer -move_time 100 -game_time 100 > results/global_global_game_time_100.txt
python3 main.py -player1 GlobalTimeABPlayer -player2 GlobalTimeABPlayer -move_time 200 -game_time 200 > results/global_global_game_time_200.txt
python3 main.py -player1 GlobalTimeABPlayer -player2 GlobalTimeABPlayer -move_time 500 -game_time 500 > results/global_global_game_time_500.txt

echo 'Testing different players vs. simple'
python3 main.py -player1 MinimaxPlayer -player2 SimplePlayer -move_time 15 > results/minimax_simple_move_time_15.txt
python3 main.py -player1 SimplePlayer -player2 MinimaxPlayer -move_time 15 > results/simple_minimax_move_time_15.txt
python3 main.py -player1 AlphabetaPlayer -player2 SimplePlayer -move_time 15 > results/alphabeta_simple_move_time_15.txt
python3 main.py -player1 SimplePlayer -player2 AlphabetaPlayer -move_time 15 > results/simple_alphabeta_move_time_15.txt

echo 'Done!'
