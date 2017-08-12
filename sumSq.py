#! /usr/bin/python
# Second prog modified: sum of square : sumSq.py
n = input("Enter a +ve integer: ")
if n>=0:
        if n == 0 or n == 1: print n,'\b^2 =', n
        else: print '1^2+...+',n,'\b^2 = ',n*(n+1)*(2*n+1)/6
else:
	print '-ve number'
