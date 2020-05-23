from turtle import *
import turtle
setup(650.650,300.300)
penup()
fd(-100)
pendown()
pensize(5)
for i in range(18):
    pencolor("purple")
    fd(-20)
    right(90)
    pencolor("pink")
    circle(-10,340)
    left(60)
    pencolor("purple")
    fd(22)
    left(90)
    pencolor("green")
    circle(-250,10)
    right(90)
done
