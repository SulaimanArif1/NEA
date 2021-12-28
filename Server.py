#SERVER SCRIPT
from Config import *
import socket
from _thread import *
import sys
from Config import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("waiting for a connection, Server started.")

def threadedClient(conn):
    conn.send(str.encode("connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", data)
                print("Sending: ", data)

            conn.sendall(str.encode(reply))
        
        except:
            break

    print("lost connection")
    conn.close

while True:
    conn, addr = s.accept()
    print("connected to: ", addr)
    start_new_thread(threadedClient, (conn,))