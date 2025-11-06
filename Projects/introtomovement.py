# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, time, random
def set_background(image_filename):
    screen = turtle.Screen()
    try:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)

def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x,y)
    window.update()
    return sprite

window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
set_background("castle")
s1 = create_sprite("character1",0,-200)

# Section 3: define movement controls
def move_w():
    s1.setheading(90)
    s1.forward(10)
        
def move_s():
    s1.setheading(270)
    s1.forward(10)
    
def move_a():
    s1.setheading(180)
    s1.forward(10)
    
def move_d():    
    s1.setheading(0)
    s1.forward(10)

window.onkeypress(move_w, "w")
window.onkeypress(move_s, "s")
window.onkeypress(move_a, "a")
window.onkeypress(move_d, "d")

# Section 4: define other controls
# hide and show controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")


# Section 5: game loop
window.listen()
while True:
    time.sleep(0.1)
    window.update()