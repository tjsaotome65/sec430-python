#!/usr/bin/python
__author__ = 'kilroy'
#  (c) 2014, WasHere Consulting, Inc.
#  Written for Infinite Skills

"""

This Form test program posts data to a hosted web form

"""
import urllib2
import urllib

url = "http://httpbin.org/post"
# data = {'txtName' : 'saotome', 'btnSearch' : 'search-results?as_q='}
data = {'comments' : 'Hellow World', 'custmail' : 'no-reply@rwu.edu', \
        'custtel' : '401-297-1000', 'delivery' : 'One Ferry Rd', \
        'size' : 'large"' }
params = urllib.urlencode(data)
req = urllib2.Request(url, data=params)
handle = urllib2.urlopen(req)
page = handle.read()
print(page)
