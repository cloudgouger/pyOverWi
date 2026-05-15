# pyOverWi (as in WiFi or Wire)
import os
import subprocess
import socket
from server import serverCode
from client import clientCode

# input ip & port

print("Input your server/client IP: ")
userIP = input()

print("Input your server/client port: ")
userPort = input()

print("Server or client? : ")
choice = input()
if choice == "client": 
    print("using client code")
    clientCode(userIP, userPort)
else:
    print("using server code")
    serverCode(userIP, userPort)






