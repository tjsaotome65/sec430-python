#!/usr/bin/python
__author__ = 'kilroy'
#  (c) 2014, WasHere Consulting, Inc.
#  Written for Infinite Skills

import httplib
import base64
import string

#
# DISCLAIMER - This encoded token method does not work on the RWU web site
#              because the security method that RWU web site expects and the i
#              methond we user are not compatible

h = "bridges.rwu.edu"
u = "tsaotome"
p = "P4ssw0rd"

# Encode the password with Base64 encoding - this is not the same thing as encryption

authToken = base64.encodestring('%s:%s' % (u, p)).replace('\n', '')
print(authToken)

req = httplib.HTTPS(h)
req.putrequest("GET", "/index.html")
req.putheader("Host", h)
req.putheader("Authorization", "Basic %s" % authToken)
req.endheaders()
req.send("")

statusCode, statusMsg, headers = req.getreply()
print("Response: ", statusMsg)
