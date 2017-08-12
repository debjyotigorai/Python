# arithMean.py: Finds arithmetic Mean
n = input(’Enter the data count: ’)
print ’Enter’,n,’data’
sum = input()
i=2
while(i<=n):
    sum = sum + input()
    i = i + 1
print ’AM = ’, sum/float(n)
