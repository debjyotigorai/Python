#! /usr/bin/python
# This is the second Python program
n = input("Enter a +ve integer: ")
if n>=0:
        if n < 2: print n, '=', n*(n+1)/2
        else: print '1+...+',n,'=',n*(n+1)/2
else:
	print '-ve number'
# file: second.py
