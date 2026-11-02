# import turtle
# for x,y,r in [(200,200,50),(-200,-200,30),(100,100,50)]:
#     turtle.penup()
#     turtle.goto(x,y)
#     turtle.pendown()
#     turtle.circle(r)
#     turtle.write(str((x,y)))
import turtle
# def add(a,b):
#     result=a+b
#     return result
# a=add(100,10)
# print(a)
#
# print("hello")
# print(add("정","진영"))
#control alt e 커서를 거기에 대고 하면 한줄 실행가능
#드래그를 해서 해도 그 줄만 실행 가능

# def sum_and_mul(a,b):
#     return a+b,a*b
#
# a=sum_and_mul(3,4)
# print(a)
#
# sum,mul = sum_and_mul(3,4)
#
# print('sum= %d'%sum)
# print('mul= %d'%mul)
#
# b= 100
# c=200
# print(b)
# print(c)
# b,c=c,b #ㅈㄴ쉽게 스왑하는법
# print(b)
# print(c)

import turtle as t
import random

def drunken_move():
    t.setheading(random.randint(0, 360))
    t.fd(random.randint(50, 300))
    t.stamp()
def restart():
    turtle.reset()

t.shape("turtle")
t.speed(1000)
t.onkey(drunken_move,' ')
t.onkey(restart,'Escape')
t.listen()

t.exitonclick() # 창 바로 안꺼지는 함수


