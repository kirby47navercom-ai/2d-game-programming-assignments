import random
import turtle as t

def drunken_move1():
    t.setheading(90)
    t.fd(50)
    t.stamp()
def drunken_move2():
    t.setheading(180)
    t.fd(50)
    t.stamp()
def drunken_move3():
    t.setheading(270)
    t.fd(50)
    t.stamp()
def drunken_move4():
    t.setheading(360)
    t.fd(50)
    t.stamp()

def restart():
    t.reset()

t.shape("turtle")

t.onkey(drunken_move1,'w')
t.onkey(drunken_move2,'a')
t.onkey(drunken_move3,'s')
t.onkey(drunken_move4,'d')

t.onkey(restart,'Escape')
t.listen()

t.exitonclick()