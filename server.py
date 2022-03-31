# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 14:47:35 2022

@author: Jonathan
"""

import socket

#take the server name  
host='localhost' 
 
#take the port number 
port=5000 
 
#create a socket at server side using TCP/IP protocol 
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
 
#bind the socket with server server and port numner 
s.bind((host,port)) 

#Makes the server listen for connections
s.listen() 


while True:
    print("Listening for connection...")
    
    data, source = s.accept()
    print("Connect with", source, "established!")
    
    print("You can provide up to two activities, separating them with a space.")
    print("To end the conversation, just type 'nothing'.")
    action = input("Suggest activity: ")
    
    msg_send = action.encode("utf-8")
    data.send(msg_send)
    
    #Returns to top of while-loop if recieve 'nothing'
    if action == "nothing": 
        continue
    
    #This block of code is to format the output based on if theres one or two activities suggested:
    action = action.split()
    if len(action) == 1:
        print("\n" + "Do you want to {}?".format(action[0]))
    else:
        print("\n" + "Do you want to " + action[0] + " or " + action[1])
    
    
    while True:
        some_msg = data.recv(1024).decode("utf-8")
        print(some_msg)
        
        response_msg = input("Suggest new activities: ")
        
        
        msg_send = response_msg.encode("utf-8")
        data.send(msg_send)
        
        if response_msg == "nothing":
            break
        
        response_msg = response_msg.split()
        if len(response_msg) == 1:    
            print("\n" + "Hey, lets {}!".format(response_msg[0]))
        else:
            print("\n" + "I want to " + response_msg[0] + " or " + response_msg[1] + ".")
        
        

msg_send = "Bye Received, connection ended.".encode("utf-8")
data.send(msg_send)
data.close()      