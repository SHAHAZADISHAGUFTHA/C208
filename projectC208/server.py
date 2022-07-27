import socket
from threading import Threading
from tkinter import *
from tkinter import ttk

PORT = 3027
IP_ADRRESS = "127.0.0.1"
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def setup():
    print("\n\t\t\t\t\t\t Music App\n")
    global PORT
    global IP_ADDRESSES
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCKSTREAM)
    SERVER.BIND((IP_ADDRESS, PORT))

    SERVER.listen(100)

    print("\t\t\t\t SERVER IS WAITING FOR CONNECTIONS")
    print("\n")

def acceptConnections():
    global SERVER
    global clients
    while True:
        client, adr = SERVER.accept()
        print(client.addr)
        