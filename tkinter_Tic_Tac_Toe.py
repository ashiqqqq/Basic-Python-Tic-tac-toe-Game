# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:31:48 2019

@author: ashiq
"""

from tkinter import *
from tkinter import messagebox

#global Variable
player = 1 
bx1 = ' '
bx2 = ' '
bx3 = ' '
bx4 = ' '
bx5 = ' '
bx6 = ' '
bx7 = ' '
bx8 = ' '
bx9 = ' '
count = 0

# root variable
root = Tk()
root.title('Tic Tac Toe')
root.geometry("290x258")

# Start Code
button1 = Button(root, text = "  ",command = lambda:activate(1))
button1.grid(row='0',column="0",ipadx="40",ipady="30")

button2 = Button(root, text = "  ",command = lambda:activate(2))
button2.grid(row='0',column="1",ipadx="40",ipady="30")

button3 = Button(root, text = "  ",command = lambda:activate(3))
button3.grid(row='0',column="2",ipadx="40",ipady="30")

button4 = Button(root, text = "  ",command = lambda:activate(4))
button4.grid(row='1',column="0",ipadx="40",ipady="30")

button5 = Button(root, text = "  ",command = lambda:activate(5))
button5.grid(row='1',column="1",ipadx="40",ipady="30")

button6 = Button(root, text = "  ",command = lambda:activate(6))
button6.grid(row='1',column="2",ipadx="40",ipady="30")

button7 = Button(root, text = "  ",command = lambda:activate(7))
button7.grid(row='2',column="0",ipadx="40",ipady="30")

button8 = Button(root, text = "  ",command = lambda:activate(8))
button8.grid(row='2',column="1",ipadx="40",ipady="30")

button9 = Button(root, text = "  ",command = lambda:activate(9))
button9.grid(row='2',column="2",ipadx="40",ipady="30")


def activate(button):
    global count 
    global bx1
    global bx2
    global bx3
    global bx4
    global bx5
    global bx6
    global bx7
    global bx8
    global bx9
    global player
    
    count += 1
    if button == 1 and player ==1:
        button1.config(text = 'X')
        player = 2
        bx1= 'X'
        button1['state'] = 'disable'
        checkend()
    elif button ==1 and player ==2:
        button1.config(text = 'O')
        player = 1
        bx1 = 'O'
        button1['state'] = 'disable'
        checkend()
        
    elif button == 2 and player ==1:
        button2.config(text = 'X')
        player = 2
        bx2 = 'X'
        button2['state'] = 'disable'
        checkend()
    elif button ==2 and player ==2:
        button2.config(text = 'O')
        player = 1
        bx2 = 'O'
        button2['state'] = 'disable'
        checkend()
        
    elif button == 3 and player ==1:
        button3.config(text = 'X')
        player = 2
        bx3 = 'X'     
        button3['state'] = 'disable'
        checkend()
    elif button ==3 and player ==2:
        button3.config(text = 'O')
        player = 1
        bx3 = 'O'
        button3['state'] = 'disable'
        checkend()
        
    elif button == 4 and player ==1:
        button4.config(text = 'X')
        player = 2
        bx4 = 'X'
        button4['state'] = 'disable'
        checkend()
    elif button ==4 and player ==2:
        button4.config(text = 'O')
        player = 1
        bx4 ='O'
        button4['state'] = 'disable'
        checkend()
        
    elif button == 5 and player ==1:
        button5.config(text = 'X')
        player = 2
        bx5 = 'X'      
        button5['state'] = 'disable'
        checkend()
    elif button ==5 and player ==2:
        button5.config(text = 'O')
        player = 1
        bx5 = 'O'
        button5['state'] = 'disable'
        checkend()
        
    elif button == 6 and player ==1:
        button6.config(text = 'X')
        player = 2
        bx6 ='X'
        button6['state'] = 'disable'
        checkend()
    elif button ==6 and player ==2:
        button6.config(text = 'O')
        player = 1
        bx6 = 'O'      
        button6['state'] = 'disable'
        checkend()
        
    elif button == 7 and player ==1:
        button7.config(text = 'X')
        player = 2
        bx7 = 'X'       
        button7['state'] = 'disable'
        checkend()
    elif button ==7 and player ==2:
        button7.config(text = 'O')
        player = 1
        bx7 ='O'     
        button7['state'] = 'disable'
        checkend()
        
    elif button == 8 and player ==1:
        button8.config(text = 'X')
        player = 2
        bx8 = 'X'    
        button8['state'] = 'disable'
        checkend()
    elif button ==8 and player ==2:
        button8.config(text = 'O')
        player = 1
        bx8 ='O'      
        button8['state'] = 'disable'
        checkend()
        
    elif button == 9 and player ==1:
        button9.config(text = 'X')
        player = 2
        bx9 = 'X'    
        button9['state'] = 'disable'
        checkend()
    elif button ==9 and player ==2:
        button9.config(text = 'O')
        player = 1
        bx9 = 'O'  
        button9['state'] = 'disable'
        checkend()
        
def checkend():
    checkrow()
    checkcol()
    checkdig()
    checktie()
    
def checkrow():
    if bx1 == bx2 == bx3 != ' ':
#        button1['state'] = button2['state'] = button3['state'] = ['enable']
        messagebox._show('Game End', 'PLAYER'+ ' ' + bx1 + ' '+  'WINS')
        exit(0)
    if bx4 == bx5 == bx6 != ' ':
#        button1['state'] = button2['state'] = button3['state'] = ['enable']
        messagebox._show('Game End', 'PLAYER'+ ' ' + bx4 + ' '+  'WINS')
        exit(0)
    if bx7 == bx8 == bx9 != ' ':
#        button1['state'] = button2['state'] = button3['state'] = ['enable']
        messagebox._show('Game End', 'PLAYER'+ ' ' + bx7 + ' '+  'WINS')
        exit(0)
        
def checkcol():
    if bx1 == bx4 == bx7 != ' ':
#        button1['state'] = button2['state'] = button3['state'] = ['enable']
        messagebox._show('Game End', 'PLAYER'+ ' ' + bx1 + ' '+  'WINS')
        exit(0)
    if bx2 == bx5 == bx8 != ' ':
#        button1['state'] = button2['state'] = button3['state'] = ['enable']
        messagebox._show('Game End', 'PLAYER'+ ' ' + bx2 + ' '+  'WINS')
        exit(0)
    if bx3 == bx6 == bx9 != ' ':
#        button1['state'] = button2['state'] = button3['state'] = ['enable']
        messagebox._show('Game End', 'PLAYER'+ ' ' + bx3 + ' '+  'WINS')
        exit(0)
        
def checkdig():
    if bx1 == bx5 == bx9 != ' ':
#        button1['state'] = button2['state'] = button3['state'] = ['enable']
        messagebox._show('Game End', 'PLAYER'+ ' ' + bx1 + ' '+  'WINS')
        exit(0)
    if bx3 == bx5 == bx7 != ' ':
#        button1['state'] = button2['state'] = button3['state'] = ['enable']
        messagebox._show('Game End', 'PLAYER'+ ' ' + bx3 + ' '+  'WINS')
        exit(0) 
    
    
def checktie():
    if count == 9:
        messagebox._show('Game End', 'We have a Tie')
        exit(0)
        

        
root.mainloop()        