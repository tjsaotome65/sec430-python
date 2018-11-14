#!/usr/bin/python
__author__ = 'kilroy'
#  (c) 2014, WasHere Consulting, Inc.
#  Written for Infinite Skills

import urllib

print("starting download")

urllib.urlretrieve("https://www.rwu.edu/sites/default/.../summer_nonmatrix_regform.pdf", "summer-registration.pdf")

print("completed")