import os
import subprocess
import socket

def serverCode(userIP, userPort):
    print(f"Connecting to {userIP}:{userPort}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connectingSocket:
        connectingSocket.bind((userIP, int(userPort)))
        connectingSocket.listen()
        connectionSocket, address = connectingSocket.accept()
        print("connected")
        with connectionSocket:
            receivedScript = connectionSocket.recv(65536)
            decodedScript = receivedScript.decode()
            with open("toRun.py", "w") as file:
                file.write(decodedScript)
            scriptOutput = subprocess.Popen(["python", "toRun.py"], stdout=subprocess.PIPE)
            for x in iter(scriptOutput.stdout.readline, b""):
                connectionSocket.sendall(x)
            connectionSocket.sendall(b"END")
            connectionSocket.close()

