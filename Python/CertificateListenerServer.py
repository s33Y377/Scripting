import socket
import ssl
import multiprocessing
shost = "192.168.16.129"
sport = "10000"
Socket_Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Socket_Server_Address = (shost, sport)
Socket_Server.bind(Socket_Server_Address)
Socket_Server.listen(100)
TLS_socket = ssl.wrap_socket(
    Socket_Server, certfile='/home/sarvesh/NII/Certificate/selfsigned.crt', keyfile='/home/sarvesh/NII/Certificate/selfsigned.key', ssl_version=ssl.PROTOCOL_SSLv23)
Server_PID = multiprocessing.current_process().pid
print("[+] Starting Server (SSL) => " + "192.168.16.129" +
      ":" + str(10000) + " || PID:" + str(Server_PID))
while (True):
    try:
        (Connection, agentAddress) = TLS_socket.accept()
        print("[+] Client Connected: " +
              agentAddress[0] + ":" + str(agentAddress[1]))
    except:
        Connection.close()
