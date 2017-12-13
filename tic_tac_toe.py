#!/usr/bin/env python3.6
#----------------------------------------
#Tic Tac Toe in Python
#Author: Joseph Skrzysowski
#Date 12/13/17
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
"""

def display_instructions():
    """Game Instructions and Header."""
    print(
    """
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
    """
    )

def tic_tac_toe():
    """
    Main function to play game. Defines the board and the combination of moves needed to win.
    """
    display_instructions()
    board = [None] + list(range(1, 10))
    winning_combos = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    ]

    def draw_board():
        """
        Draws/prints the board layout like the number pad on your computer
        """
        print(board[7], board[8], board[9])
        print(board[4], board[5], board[6])
        print(board[1], board[2], board[3])


    def choose_number():
        """
        Function that runs a while loop for handling the user input.
        """
        while input: #I could just test for True here, but I want to be clear for now
            try:
                i = int(input())
                if i in board:
                    return i
                else:
                    print("\nNot a valid move. Try again")
            except ValueError:
                print("\nNot a number. Try again")

    def stop_game():
        """
        Runs draw_board()-prints the board layout like the number pad on your computer. Tests & tracks the placement of players 'X' & 'O'.
         """
        for row1, row2, row3 in winning_combos:
            if board[row1] == board[row2] == board[row3]:
                print("Player {0} is the winner!\n".format(board[row1]))
                print("Tadow!!!\n")
                return True
        num = 9 #My linter seems to be very picky about not assigning 9 to a variable
        if num == sum((placement == 'X' or placement == 'O') for placement in board):
            print("Tie!!!\n")
            return True

    for player in ['X', 'O'] * 9:
        draw_board()
        if stop_game():
            break
        print("Player {0} pick your square".format(player))
        board[choose_number()] = player
        print()
    board = [None] + list(range(1, 10))
while tic_tac_toe: #I could just test for True here, but I want to be clear for now
    tic_tac_toe()
    if input("Want to play again? (y/n)\n") != "y":
        break
