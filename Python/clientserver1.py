#!/usr/bin/python           # This is server.py file
import socket               # Import socket module
import os
import time as t

# open socket
s = socket.socket()         # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 9500

if os.fork() == 0:
    # server
    print('about to listen')
    while 1:
        s.listen(1)
        c = s.accept()
        cli_sock, cli_addr = c
        cli_sock.send("Hello to you! %s" % cli_addr)
elif os.fork() == 0:
    t.sleep(1)
    # client
    print('in here2')
    s.bind((host, port))        # Bind to the port
    s.connect((host, port))
    s.send("Hello!\n")
    print(s.recv(9500))
    s.close()
