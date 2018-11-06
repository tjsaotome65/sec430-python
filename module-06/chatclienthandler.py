"""
File: chatclienthandler.py
Project 10.10
Client handler for chatroom. Receives ThreadSafeTranscript object from
the server, handles requests from client.
"""

from socket import *
from codecs import decode
from threading import Thread
from time import ctime

BUFSIZE = 1024
CODE = "ascii"

class ChatClientHandler(Thread):
    """Handles chatroom requests from a client."""
    
    def __init__(self, client, transcript):
        """Save references to the client socket and shared transcript."""
        Thread.__init__(self)
        self.client = client
        self.transcript = transcript
   
    def run(self):
        """Obtains name from the client, then enters
        an interative loop to take and respond to
        requests."""
        # Establish the client's name.
        self.name = decode(self.client.recv(BUFSIZE), CODE)
        if not self.name:
            print("Client disconnected")
            self.client.close()
        else:
            print(self.name, "is connected")
            # Push the entire transcript to the client
            # Add the client's time-stamped message to shared transcipt 
            while True:
                self.client.send(bytes(str(self.transcript), CODE))
                message = decode(self.client.recv(BUFSIZE), CODE)
                if not message or message == "LOGOUT":
                    message = self.name + " has disconnected at " + ctime() + '\n'
                    self.transcript.add(message)
                    self.client.close()
                    break
                else:
                    message = self.name + '\n' + ctime() + '\n' + message + '\n'
                    self.transcript.add(message)
