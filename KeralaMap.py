import turtle


# ******** Graphics Methods to plot map and connection line between two districts

# *********Method used to plot kerala Map*************
def map_display(districts):
    screen = turtle.Screen()
    screen.title('Kerala Districts')
    screen.setup(height=1800, width=800)
    image = 'KeralaStates.gif'
    screen.addshape(image)
    turtle.shape(image)

    for district in districts:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        dname = district[0]
        x, y = district[1], district[2]
        t.goto(int(x), int(y))
        t.write(dname, font=('Calibri', 8, "bold"))


# *********Method used to connect districts in kerala Map*************
def line_display(origin, destination):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.width(4)
    t.goto(origin[0], origin[1])
    t.pendown()
    t.goto(destination[0], destination[1])
