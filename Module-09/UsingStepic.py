#!/usr/bin/python
__author__ = 'kilroy'
#  (c) 2014, WasHere Consulting, Inc.
#  Written for Infinite Skills

"""

Stepic example - this example uses JPEG image for Stegonography

"""
# need PIL and stepic packages
import Image, stepic

i = Image.open("bullpuppies.jpg")  # The JPEG image has to exist.  It can be any JPEG.
i.show()
#  could open a file here
# f = open("myfile", "r")
# text = f.read()

steg = stepic.encode(i, "This is some text")
# steg = stepic.encode(i, text)

steg.save("steg.jpg", "JPEG")

i2 = Image.open("steg.jpg")
i2.show()
