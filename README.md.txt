Created 31.03.2022 by Jonathan Risung


This is my work for the individual portfolio assignment 1 in DATA2410-1 22V.

The three other files in this directory are:
client.py (which is for task 1)
server.py (which is for task 2)
bots.py (which is the bots used for this assignment)


Task 1:
When making client.py I made it possible to choose using all bots through one client. 
This was firstly for testing purposes, but I thought it made for a good addition, so I decided to keep it.
There's not much more to say about this task, as I believe the code is quite self explanatory.


Task 2:
When creating the server file, I took inspiration from the teaching assisstant's code in lab 11 and 12. And tried to implement some code 
from https://www.positronx.io/create-socket-server-with-multiple-clients-in-python/
However, this proved unsuccsessful. 

The server therefore doesn't work with multiple clients at one time. But with the implementation from task 1, there is still possible to 
chat with multiple bots at the same time anyway. 

I made it so that by typing 'nothing' at server side will disconnect the current client, and search for the next possible connection.