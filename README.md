# tic_tac_toe

![short demo/giphy of tic-tac-toe game](https://raw.githubusercontent.com/josephskrzysowski/tic_tac_toe/master/img/tic_tac_toe.gif?raw=true)


## Overview
#Python3.6 env
#To run you can:
#python ./tic_tac_toe.py
#Or run
#sudo chmod +x tic_tac_toe.py
#./tic_tac_toe.py
#----------------------------------------
"""
1) display instructions/rules for playing the game
2) create main function for holding all the functionality for the game
3) define the board using numbers like a key pad using range()
4) define the winning_combos variable. Which combo of 3 choices define a winner
5) print board layout while nobody's won or its not a tie
6) ask user to choose a number input using one function to handle both players
7) insert user input on the board(update the board)
8) test for winning combination
9) if game is over run main function unless player choses to quit


    _____      ___       ____    _     ___     ____   ___   ___
   /_   _\ _  /  _\     /_  _\  / \   /  _\   /_  _\ /   \ |  _|
     | |  | | | |__ --   | |   / | \  | |_  --  | |  | | | | -_
     |_|  |_| \___/      |_|  /_ |_ \ \___/     |_|  \___/ |___|

    Welcome to Tic-Tac-Toe.
    Make your move by entering a number, 1 - 9.  The number
    will correspond to the board position like this:

                    7 | 8 | 9
                    ---------
                    4 | 5 | 6
                    ---------
                    1 | 2 | 3
    Player 1 is X
    Player 2 is O
    Three in a Row Wins!