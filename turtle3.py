from turtle import Turtle, mainloop, Screen

def tree(plist, l, a, f):
    
    if l > 3:
        lst = []
        for p in plist:
            p.forward(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        for x in tree(lst, l*f, a, f):
            yield None

def maketree():
    p = Turtle()
    p.pencolor("green")
    p.setundobuffer(None)
    p.hideturtle()
    p.speed(0)
    p.tracer(30,0)
    p.left(90)
    p.penup()
    p.forward(-210)
    p.pendown()
    t = tree([p], 200, 65, 0.6375)
    for x in t:
        pass

s = Screen()
maketree()
print s.getcanvas().postscript()
