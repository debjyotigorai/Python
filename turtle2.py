from turtle import *

s = Screen()
s.setworldcoordinates(-22,-22,22,22)

pencolor("green")

for i in range(24):
    circle(10)
    rt(15)

print s.getcanvas().postscript()
