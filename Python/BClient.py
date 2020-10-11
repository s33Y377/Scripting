#!/usr/bin/env python3

# from socket import *
from socket import AF_INET, socket, SOCK_STREAM, SOL_SOCKET
from threading import Thread
import ssl


def receive():
    while True:
        msg = conn.recv(BUFSIZ).decode("utf8")
        print("msg", msg)
        if msg == "{quit}":
            conn.close()
            break
        if not msg:
            break
        print(msg)


def send():
    while True:
        msg = input()
        print("msg", msg)
        conn.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            break


host_addr = '192.168.16.129'
host_port = 33000
server_sni_hostname = 'www.bluescope.com'
server_cert = 'server.crt'
client_cert = 'client.crt'
client_key = 'client.key'

BUFSIZ = 1024

context = ssl.create_default_context(
    ssl.Purpose.SERVER_AUTH, cafile=server_cert)
context.load_cert_chain(certfile=client_cert, keyfile=client_key)

s = socket(AF_INET, SOCK_STREAM)
conn = context.wrap_socket(
    s, server_side=False, server_hostname=server_sni_hostname)
conn.connect((host_addr, host_port))

receive_thread = Thread(target=receive)
send_thread = Thread(target=send)
receive_thread.start()
send_thread.start()
receive_thread.join()
send_thread.join()
