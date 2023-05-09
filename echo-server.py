#!/usr/bin/env python3

import socket
import numpy as np

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

board=[["","",""],["","",""],["","",""]] 

def is_full(board):
    print("calclcll")

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
        return True
    if (flag_O):
        print("O has WON")
        return True
    if(is_full(board)==0):
        print("Its a DRAW")
        return True

    return False


def upd(data,pos,board):
    b = np.array(board)
    b = b.reshape(1,9)
    if(b[0][pos] != ""):
        print("Illegal Move")
        
    else:
         b[0][pos] = data
    b = b.reshape(3,3)
    board = b
    return board


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))


    s.listen()
    conn, addr = s.accept()
    with conn:
        
        while True:
            data = conn.recv(1024)
            board = upd("O",int(data.decode('utf-8'))-1,board)
            print(f"O has entered {data.decode('utf-8')} \n")
            print("Your turn \n")
            print(board)
            if checkb(board):
                break
            
            if not data:
                break
            
            inp = int(input("Enter your position [1 to 9] : "))
            board = upd("X",inp-1,board)
            print(board)
            conn.sendall(bytes(str(inp),'utf-8'))
            if checkb(board):
                break
            

