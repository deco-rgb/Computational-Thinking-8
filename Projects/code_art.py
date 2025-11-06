import turtle 
t = turtle.Turtle()
turtle.Screen().bgcolor("black")
t. goto(-50,-40)
t.color("crimson")
t.speed(10)
#comment: this is were the colors are set

for i in range (500):
    t.forward(100 + i)
    t.left(127)
    #comment: this is were the sprite makes the first shape
    #comment: made so that it repeated less

import turtle 
t2 = turtle.Turtle()
t2.goto(10,2)
t2.color("green")
t2.speed(10)

for i in range (200):
    t2.forward(2 + i)
    t2.left(127)
#comment: this is were the second shape is made
   
turtle.exitonclick()

