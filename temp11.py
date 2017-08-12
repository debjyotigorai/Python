# numAs.py : number of A’s in a string
s = input("Enter a string: ")
aCount = 0
for x in s:
    if x == ’a’ or x == ’A’:
       aCount = aCount + 1
print s, ’:’, aCount, "a’s"
