#! /usr/bin/python
# find largest among n data: largest1.py 
#
n = input("Enter a +ve integer: ")
d=raw_input("Enter data, one per line: ")
try:
   max=int(d)
   for i in range(n-1):
       d=raw_input("Enter data, one per line: ")
       try:
          data=int(d)
          if max < data: max = data
       except: print 'Not int (2)'
   print 'Max:', max
except: print 'Not int (1)'
