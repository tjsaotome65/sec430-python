"""
File: timeserver2.py
Server for providing the day and time.  Uses client
handlers to handle clients' requests.
"""

from socket import *
from timeclienthandler import TimeClientHandler

HOST = "localhost"
PORT = 5000
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

# The server now just waits for connections from clients
# and hands sockets off to client handlers
while True:
    print("Waiting for connection . . .")
    client, address = server.accept()
    print("... connected from: ", address)
    handler = TimeClientHandler(client)
    handler.start()
