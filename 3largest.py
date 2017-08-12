#! /usr/bin/python
# Largest among 3 data: 3largest.py
x = raw_input("Enter three integers: ")
y = x.split(' ')
try:
   m, n, p = int(y[0]), int(y[1]), int(y[2])
   if m < n: max=n
   else: max=m
   if max < p: max=p
   print 'Max:',max
except:
   print 'Not three integers'
