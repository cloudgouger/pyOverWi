import os
import subprocess
import socket
import sys

def clientCode(userIP, userPort):
    print(f"Connecting to {userIP}:{userPort}")
    connectingSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connectingSocket.connect((userIP, int(userPort)))
    print("connected")
    with connectingSocket:
        fileToSend = open("send.py")
        fileString = fileToSend.read()
        connectingSocket.sendall(fileString.encode())
        while True:
            receivedStdout = connectingSocket.recv(1024)
            if not receivedStdout:
                continue
            receivedStdoutDecoded = receivedStdout.decode()
            print(receivedStdout.decode())
            if receivedStdoutDecoded == "END":
                sys.exit()
            
            
