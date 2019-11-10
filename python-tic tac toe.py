# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:19:32 2019

@author: ashiq
"""

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    
player = 1 
game_still_running = True

def play_game(): 
    display_board()
    print('Player 1, please start. You are X.')
    while game_still_running == True:
        handel_turn()
        check_game_over()
        if game_still_running == True:
            flip_player()
    
def handel_turn():
    global player
    position = input("Please choose a position from 1-9:")
    position = int(position) -1
    if board[position] == '-':
        if player == 1:
            board[position] = "X"
        elif player == 2:
            board[position] = "O"
    else: 
        print('That position is taken, please choose a empty cell')
        handel_turn()
    display_board()

def flip_player():
    global player
    if player == 1:
        player = 2 
        print('It is now player 2 turn')
    elif player == 2:
        player = 1
        print('It is now player 1 turn')
    return()
    
def check_game_over():
    check_win()
    if game_still_running == True:
        check_tie()
    return()
    
    
def check_win():
    check_row()
    check_colm()
    check_dig()
    return()
    
def check_row():
    global game_still_running
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    if row1 or row2 or row3: 
        game_still_running = False
        print('Player %d wins.' % player)

def check_colm():
    global game_still_running
    colm1 = board[0] == board[3] == board[6] != '-'
    colm2 = board[1] == board[4] == board[7] != '-'
    colm3 = board[2] == board[5] == board[8] != '-'
    if colm1 or colm2 or colm3: 
        game_still_running = False
        print('Player %d wins.' % player)
        
def check_dig():
    global game_still_running
    dig1 = board[0] == board[4] == board[8] != '-'
    dig2 = board[2] == board[4] == board[6] != '-'
    if dig1 or dig2:
        game_still_running = False
        print('Player %d wins.' % player)
    
def check_tie():
    global game_still_running
    if '-' not in board:
        game_still_running = False
        print('The game is a Tie, Please try again')
    
play_game()
        
    

    
    
    
    

    
    
    
    
    
    
    
    
    
    
    