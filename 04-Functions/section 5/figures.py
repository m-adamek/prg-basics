import turtle

def draw_square(length):
    # Create a new turtle for drawing the square
    pen = turtle.Turtle()
    pen.speed(5)
    
    for _ in range(4):
        pen.forward(length)
        pen.right(90)

    # Hide the turtle after drawing
    pen.hideturtle()