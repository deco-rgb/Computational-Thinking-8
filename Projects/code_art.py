import turtle 
t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t. goto(-50,-40)
t.color("crimson")
t.speed(10)

for i in range (500):
    t.forward(100 + i)
    t.left(127)

import turtle 
t2 = turtle.Turtle()
t2.goto(10,2)
t2.color("green")
t2.speed(10)

for i in range (200):
    t2.forward(2 + i)
    t2.left(127)

   
turtle.exitonclick()
