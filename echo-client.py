#!/usr/bin/env python3

import time
import socket
import numpy as np


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

board = [["","",""],
         ["","",""],
         ["","",""]]

b = np.array(board)

def is_full(board):
    
    cnt =0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j]==""):
                cnt+=1
    return cnt

def checkb(board):
    flag_X=0
    flag_O=0

    # checking row
    for i in range(len(board)):
        count_X=0
        count_O=0
        for j in range(len(board[0])):
            if(board[i][j]=="X"):
                count_X=count_X+1
            elif(board[i][j]=="O"):
                count_O=count_O+1
            
        if(count_X==3):
            flag_X=1
        if(count_O==3):
            flag_O=1

    # checking column

    for i in range(len(board)):
        count_X=0
        count_O=0
        for j in range(len(board[0])):
            if(board[j][i]=="X"):
                count_X=count_X+1
            elif(board[j][i]=="O"):
                count_O=count_O+1
        if(count_X==3):
            flag_X=1
        if(count_O==3):
            flag_O=1

    # checking diagonal1
    count_X=0
    count_O=0
    for i in range(3):
        if(board[i][i]=="X"):
            count_X=count_X+1
        elif(board[i][i]=="O"):
            count_O=count_O+1
        if(count_X==3):
            flag_X=1
        if(count_O==3):
            flag_O=1

    # checking diagonal2
    count_X=0
    count_O=0
    j=2
    for i in range(3):
        if(board[i][j]=="X"):
            count_X=count_X+1
        elif(board[i][j]=="O"):
            count_O=count_O+1
        if(count_X==3):
            flag_X=1
        if(count_O==3):
            flag_O=1
        j=j-1


    if (flag_X):
        print("X has WON")
    if (flag_O):
        print("O has WON")
    if(is_full(board)==0):
        print("Its a DRAW")
        return True

def update(ch,x):      
    
    row = (int(x)-1) // 3
    column = (int(x)-1) % 3
    
    if(board[row][column] == ""):
        board[row][column] = ch
    else:
        msg = "The position is reserved. Select a different position"
        print(msg)
        x = input("Enter your position [1 to 9] : ")
    return board

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        x = input("Enter your position [1 to 9] : ")

        board = update("O",x)
        print(np.array(board))
        
        s.sendall(bytes(x, 'utf-8'))
        if checkb(board):
            break
        data = s.recv(1024)
        board = update("X", data.decode('utf-8'))
        
        
        print(f"X has entered {data.decode('utf-8')} \n")
        print(np.array(board))
        if checkb(board):
            break
        print("Your turn \n")

        
       