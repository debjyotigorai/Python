#! /usr/bin/python
# Larger of two: mnTonm.py
x = raw_input("Enter a 2-digit +ve integer: ")
if len(x) == 2 and x.isdigit():
	y = x[1]+x[0]
	print x,'-->',y
else:
	print 'Not a 2-digit integer'


