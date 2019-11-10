# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:44:24 2019

@author: ashiq
"""

""" tic tac toe game - Basic Creation"""
# Display board 
# play game - put x or o in a potential box(colm, row)
# check valid 
# if true - check win 
# check win
    # check 3 in a colm 
    # chcek 3 in a row
    # check diagonal 
# if true - end game - disply msg - winner 
    #else - switch player - display player # turn
    
    #repeat


    
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    


def handel_turn(player):
    position = input('Please choose a position from 1-9: ')
    position = int(position) -1
    if board[position] == '-':
        if player == 1:
            board[position] = "X"
        elif player == 2:
            board[position] = "O"
    else: handel_turn()


    
def check_game_over():
    check_win()
    check_tie()
  
    
    
def check_win():
    
    
    return (game_still_going == False)

    
def check_tie():
    
    
    return( game_still_going == False)
    
    
def flip_player():
    counter = 0 
    if counter//2 ==1 :
        player = 1
        print('Player 1 Turn - You are X')
    else: 
        player = 2 
        print('Player 2 Turn - You are O')
    counter =+1 
    
    
    
    
def check_win():
    return()
    
def play_game():
    # display board to start the game 
    display_board()
    flip_player()
    # create a loop so the game only stops when someone wins or its a tie
    #while game_still_going = True:
    handel_turn(player)
    check_game_over()
    
        

    
play_game()
    