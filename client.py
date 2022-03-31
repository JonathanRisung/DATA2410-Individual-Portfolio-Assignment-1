# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 14:55:50 2022

@author: Jonathan
"""

import sys
import socket

#imports all functions from bots.py
import bots


# TCP Client program to chat with bots

# IP from command line arguments
host = sys.argv[1]

# Port from command line arguments
port = int(sys.argv[2])

# Chooses bot: (Tests if bot is chosen in command line arguments, if not use all)
try: 
    bot = str(sys.argv[3])
except:
    bot = "alle"


#Creates a socket at server side with TCP/IP protocol
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connects to server and port
c.connect((host,port))


while True:
    #receives message from server
    msg_recv = c.recv(1024).decode("utf-8")
    print(msg_recv)
    
    if msg_recv == "nothing":
        break
    
    
    #Splits message string into list
    msg_recv = msg_recv.split()
    
    if bot == "erling": #if-check to choose bot
        if len(msg_recv) == 1: #Checks if one or two arguments
            response = "Erling: {}".format(bots.erling(msg_recv[0]))
        else:
            response = "Erling: {}".format(bots.erling(msg_recv[0], msg_recv[1]))
    elif bot == "sebastian":
        if len(msg_recv) == 1:
            response = "Sebastian: {}".format(bots.sebastian(msg_recv[0]))
        else:
            response = "Sebastian: {}".format(bots.sebastian(msg_recv[0], msg_recv[1]))
    elif bot == "dan":
        response = "Dan: {}".format(bots.dan(msg_recv[0]))
    elif bot == "enrique":
        if len(msg_recv) == 1:
            response = "Enrique: {}".format(bots.enrique(msg_recv[0]))
        else:
            response = "Enrique: {}".format(bots.enrique(msg_recv[0], msg_recv[1]))
    elif bot == "alle":
        if len(msg_recv) == 1:
            response = "Erling: {}".format(bots.erling(msg_recv[0]) + "\n")
            response += "Sebastian: {}".format(bots.sebastian(msg_recv[0]) + "\n")
            response += "Dan: {}".format(bots.dan(msg_recv[0]) + "\n")
            response += "Enrique: {}".format(bots.enrique(msg_recv[0]) + "\n")
        else:
            response = "Erling: {}".format(bots.erling(msg_recv[0], msg_recv[1]) + "\n")
            response += "Sebastian: {}".format(bots.sebastian(msg_recv[0], msg_recv[1]) + "\n")
            response += "Dan: {}".format(bots.dan(msg_recv[0], msg_recv[1]) + "\n")
            response += "Enrique: {}".format(bots.enrique(msg_recv[0], msg_recv[1]) + "\n")
        
    print(response)   #print response client side 
    res_send = response.encode("utf-8") #encodes response
    c.send(res_send) #sends response to server
    
c.close()
    
    