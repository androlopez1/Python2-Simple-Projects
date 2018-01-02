import turtle

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(10)
    for i in range (1,37):
        draw_square (brad)
        brad.right(10)
    for i in range(1,3):
        brad.forward(100)
        brad.right(120)
    brad.right(210)
    brad.forward(100)
    window.exitonclick()

draw_art()

