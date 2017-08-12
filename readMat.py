#readMat.py : read matrix in row major order
def readMat(r, c, m):   # readMat.py
    tl = raw_input("Enter the matrix in row major order: ")
    tl = tl.split(' ')
    k = 0
    for i in range(r):
        lr = list()
        for j in range(c):
            lr = lr + [float(tl[k])]
            k = k+1
#        lr = float(tl[c*i+j]) for j in range(c)
        m.append(lr)
    return m
    
r = input("Enter number of rows: ")
c = input("Enter number of columns: ")
m = list()
readMat(r,c,m)
print m
