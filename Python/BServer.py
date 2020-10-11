#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET
from threading import Thread
import ssl


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = conn.accept()
        print("%s:%s has connected." % client_address)
        print("client", client)
        client.send(
            bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        print("addresses[client]", addresses[client])
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = client.recv(4096)
    # print("name", name)
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(1024)
        if msg != bytes("{quit}", "utf8"):
            # print("msg", type(msg))
            # print("name", type(name))
            print(name, msg)
            # broadcast(bytes(msg, name + ": "))
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)


clients = {}
addresses = {}

HOST = ''
PORT = 33000
ADDR = (HOST, PORT)

server_cert = 'server.crt'
server_key = 'server.key'
client_certs = 'client.crt'


context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.verify_mode = ssl.CERT_REQUIRED
context.load_cert_chain(certfile=server_cert, keyfile=server_key)
context.load_verify_locations(cafile=client_certs)

bindsocket = socket(AF_INET, SOCK_STREAM)
bindsocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
bindsocket.bind((HOST, PORT))

conn = context.wrap_socket(bindsocket, server_side=True)

if __name__ == "__main__":
    conn.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    bindsocket.close()
