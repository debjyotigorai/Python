#addMat.py : adds two matrices
def matAdd(a,b):     #addMat.py
    r = len(a)
    c = len(a[0])
    d = list()
    for i in range(r):
        tl = list()
        for j in range(c):
            tl.append(a[i][j]+b[i][j])
#        tl = [a[i][j]+b[i][j] for j in range(c)]
        d.append(tl)
#    d = [a[i][j]+b[i][j] for j in range(c)] for i in range(r)]
    return d
def readMat(r, c, m):   #readMat.py
    tl = raw_input("Enter the matrix in row-major order: ")
    tl = tl.split(' ')      #addMat.py
    k = 0
    for i in range(r):
        lr = []
        for j in range(c):
            lr = lr + [float(tl[k])]
            k = k + 1
        m.append(lr)
    return m
    
    
r = input("Enter number of rows: ")
c = input("Enter number of columns: ")
print "Enter matrix A: "
a = list()
readMat(r,c, a)
print "Enter matrix B: "
b = list() 
readMat(r,c, b)
c = matAdd(a,b)
print "A:", a
print "B:", b
print "C:", c
