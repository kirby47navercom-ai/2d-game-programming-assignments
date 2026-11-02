import turtle
import random

# count = 12
# while count > 0:
#     turtle.forward(100)
#     turtle.left(30)
#     count -= 1
# else:
#     print('count is zero')

# while True:
#     shape = input("enter shape: ")
#     if shape == "circle":
#         turtle.circle(50)
#     elif shape == "triangle":
#         turtle.forward(50); turtle.left(120)
#         turtle.forward(50)
#         turtle.left(120)
#         turtle.forward(50)
#     elif shape == "quit":
#         break
#     else:
#         print("Wrong Shape")
#세미콜론은 한줄에 두개를 쓰고 싶을 때 씀

turtle.shape('turtle')
while(True):
    turtle.setheading(random.randint(0,360))
    turtle.forward(random.randint(0,10))
    turtle.stamp()