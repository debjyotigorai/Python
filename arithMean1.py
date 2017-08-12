#! /usr/bin/python
# Larger of two: arithMean1.py
x = raw_input("Enter a 2-digit +ve integer: ")
if len(x) == 2 and x.isdigit():
	y = float(x[1])+float(x[0])
	print 'Mean of digits = ', y/2
else:
	print 'Not a 2-digit integer'


