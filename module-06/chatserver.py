"""
File: chatserver.py
Project 10.10
Server for providing chatroom access.
Uses client handlers to handle clients' requests.
"""

from socket import *
from chatclienthandler import ChatClientHandler
from threadsafetranscript import ThreadSafeTranscript


HOST = "localhost"
PORT = 5000
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)
# Create the shared thread-safe transcript.
transcript = ThreadSafeTranscript()

# The server now just waits for connections from clients
# and hands sockets off to client handlers
while True:
    print("Waiting for connection . . .")
    client, address = server.accept()
    print("... connected from: ", address)
    handler = ChatClientHandler(client, transcript)
    handler.start()
