#ass14.py : print the prime numbers from 2 to 1000
i=1
x = int(input("Enter the number:"))
for k in range (1, (x+1), 1):
    c=0
    for j in range (1, (i+1), 1):
        a = i%j
        if (a==0):
            c = c+1

    if (c==2):
          print (i)
    else:
          k = k-1

    i=i+1
