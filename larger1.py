#! /usr/bin/python
# Larger of two: larger1.py
x = raw_input("Enter two integers: ")
y = x.split(' ')
try:
	m, n = int(y[0]), int(y[1])
	if m < n : max=n
	else: max=m
	print 'Max(',m,',',n,')=',max
except:
	print 'Not two integers'
