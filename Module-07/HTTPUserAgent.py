#!/usr/bin/python
__author__ = 'kilroy'
#  (c) 2014, WasHere Consulting, Inc.
#  Written for Infinite Skills

"""

HTTP User Agent Demo

User agent is an identifier to the HTTP web server what program it is using to access the web server.

"""

import httplib

h = "www.google.com"

req = httplib.HTTP(h)
req.putrequest("GET", "/")
req.putheader("Host", h)
req.putheader("User-Agent", "Bogus non-standard browser: 5.6")
req.putheader("My-Header", "My value")
req.endheaders()
req.send("")

statusCode, statusMsg, headers = req.getreply()
print("Response: ", statusMsg)

