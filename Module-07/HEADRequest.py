#!/usr/bin/python
__author__ = 'kilroy'
#  (c) 2014, WasHere Consulting, Inc.
#  Written for Infinite Skills

import httplib

host = "www.google.com"

req = httplib.HTTP(host)
req.putrequest("HEAD", "/")
req.putheader("Host", host)
req.endheaders()
req.send("")

statusCode, statusMsg, headers = req.getreply()
print("Status: ", statusCode)
