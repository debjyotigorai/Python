#ass14.py : find all the prime numbers in
#given range

x = input("Enter a positive number: ")
for n in range(x+1):
        if n >= 2:
           sqrtN = int(n**0.5)
           prime = True
           for m in range(sqrtN+1)[2:]:
               if n%m == 0:
                  prime = False
                  break
           if prime: print n

