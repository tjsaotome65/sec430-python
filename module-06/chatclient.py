"""
File: chatclient.py
Project 10.10
This module defines the ChatClient class, which provides a window
for a chatroom conversation.
"""

from socket import *
from codecs import decode
from breezypythongui import EasyFrame

HOST = "localhost"
PORT = 5000
ADDRESS = (HOST, PORT)
BUFSIZE = 1024
CODE = "ascii"

class ChatClient(EasyFrame):
    """Represents an chat window for a client.
    The window waits for users to connect, then
    sends requests to the server."""

    def __init__(self):
        """Initialize the window."""
        EasyFrame.__init__(self, title = "Chat Room")
        # Create and add the widgets to the window."""
        self.outputLabel = self.addLabel(text = "Transcript of the chat:",
                                        row = 0, column = 0,
                                        columnspan = 2,
                                        sticky = "NSEW")
        self.outputArea = self.addTextArea("", row = 1, column = 0,
                                           columnspan = 2,
                                           width = 50, height = 4)
        self.inputLabel = self.addLabel(text = "Want to connect?",
                                        row = 2, column = 0,
                                        columnspan = 2,
                                        sticky = "NSEW")
        self.inputArea = self.addTextArea("", row = 3, column = 0,
                                           columnspan = 2,
                                           width = 50, height = 4)
        self.sendButton = self.addButton(text = "Send",
                                         row = 4, column = 0,
                                         command = self.send,
                                         state = "disabled")
        self.connectButton = self.addButton(text = "Connect",
                                            row = 4, column = 1,
                                            command = self.connect)
        # Connect to server and confirm connection

    def connect(self):
        """Attempts to connect to the server.  If successful,
        enables the send and disconnect buttons."""
        name = self.prompterBox(title = "Input Dialog",
                                promptString = "Your name:")
        if name == "": return
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.connect(ADDRESS)
        self.server.send(bytes(name, CODE))
        reply = decode(self.server.recv(BUFSIZE), CODE)
        if reply:
            self.outputArea.setText(reply)
            self.inputLabel["text"] = "Enter your message below:"
            self.sendButton["state"] = "normal"
            self.connectButton["text"] = "Disconnect"
            self.connectButton["command"] = self.disconnect
        else:
            self.outputArea.setText("Could not connect")            
                        
    def disconnect(self):
        """Disconnects the client, clears the text areas,
        disables the send button, and enables connect."""
        self.server.send(bytes("DISCONNECT", CODE))
        self.server.close()
        self.inputArea.setText("")
        self.outputArea.setText("")
        self.inputLabel["text"] = "Want to connect?"
        self.sendButton["state"] = "disabled"
        self.connectButton["text"] = "Connect"
        self.connectButton["command"] = self.connect

    def send(self):
        """Sends a message to the server and waits for a
        reply."""
        message = self.inputArea.getText()
        if message == "": return
        self.server.send(bytes(message, CODE))
        reply = decode(self.server.recv(BUFSIZE), CODE)
        self.outputArea.setText(reply)
        
def main(fileName = None):
    """Creates the bank with the optional file name,
    wraps the window around it, and opens the window.
    Saves the bank when the window closes."""
    ChatClient().mainloop()

if __name__ == "__main__":
    main()
