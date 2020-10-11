import socket
from threading import Thread
import ssl

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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = context.wrap_socket(
    s, server_side=False, server_hostname=server_sni_hostname)
conn.connect((host_addr, host_port))
