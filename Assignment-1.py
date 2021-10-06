import turtle
turtle.tracer(0)

x_max = 200
x_min = -200
y_max = 200
y_min = -200

turtle.setworldcoordinates(-201, -201, 201, 201)
turtle.up()
turtle.goto(x_min, y_min)
turtle.down()
for i in range(4):
    turtle.forward(400)
    turtle.left(90)
turtle.up()
turtle.home()

def draw_shape (s, c, x, y, l, h = 0):
    global past
    turtle.fillcolor(c)
    if (x < x_min) or (x > x_max) or (y < y_min) or (y > y_max):
        perimeter = 0
    turtle.goto(x, y)
    if s == 'r':
        if rectangle_will_fit(x, y, l, h):
            turtle.down()
            turtle.begin_fill()
            for i in range (2):
                turtle.forward(l)
                turtle.right(90)
                turtle.forward(h)
                turtle.right(90)
            turtle.end_fill()
            turtle.up()
            turtle.setheading(0)
            perimeter = (l + h)*2
    elif s == 't':
        if triangle_will_fit(x, y, l):
            turtle.down()
            turtle.begin_fill()
            for i in range (3):
                turtle.forward(l)
                turtle.left(120)
            turtle.end_fill()
            turtle.up()
            turtle.setheading(0)
            perimeter = 3*l
    elif s == 'c':
        if circle_will_fit(x, y, l):
            turtle.down()
            turtle.begin_fill()
            turtle.circle(l)
            turtle.end_fill()
            turtle.up()
            turtle.setheading(0)
            import math
            p = math.pi
            perimeter = p*2*l
        pass
    else:
        pass
    input("Press Enter to continue: ")
    return perimeter

def rectangle_will_fit (x, y, l, h):
    if (x < x_min) or (x > x_max) or (y < y_min) or (y > y_max) or ((x+l) < x_min) or ((x+l) > x_max) or ((y-h) < y_min) or ((y-h) > y_max):
        return False
    else:
        return True
    pass

def triangle_will_fit (x, y, l):
    if (x < x_min) or (x > x_max) or (y < y_min) or (y > y_max) or ((x+l) < x_min) or ((x+l) > x_max) or ((y+(l*(0.5)*(3**(1/3)))) < y_min) or ((y+(l*(0.5)*(3**(1/3)))) > y_max):
        return False
    else:
        return True

def circle_will_fit (x, y, l):
    if (x < x_min) or (x > x_max) or (y < y_min) or (y > y_max) or ((x-l) < x_min) or ((x+l) > x_max) or ((y+(2*l)) < y_min) or ((y+(2*l)) > y_max):
        return False
    else:
        return True

def test_draw_shape_rectangle ():
    x = 0
    y = 0
    a = draw_shape('r', 'red', x, y, 10, 20)
    c = turtle.fillcolor()
    assert(c == 'red')
    assert(int(turtle.xcor()) == x)
    assert(int(turtle.ycor()) == y)
    assert(int(turtle.heading()) == 0)
    assert(a == 60)
    print("no errors!")

def test_draw_shape_triangle ():
    x = 100
    y = -100
    a = draw_shape('t', 'yellow', x, y, 50)
    c = turtle.fillcolor()
    assert(c == 'yellow')
    assert(int(turtle.xcor()) == x)
    assert(int(turtle.ycor()) == y)
    assert(int(turtle.heading()) == 0)
    assert(a == 150)
    print("no errors!")

def test_draw_shape_circle ():
    x = -100
    y = 100
    a = draw_shape('c', 'orange', x, y, 50)
    c = turtle.fillcolor()
    import math
    perimeter = int(math.pi*2*50)
    assert(c == 'orange')
    assert(int(turtle.xcor()) == x)
    assert(int(turtle.ycor()) == y)
    assert(int(turtle.heading()) == 0)
    assert(a == perimeter)
    print("no errors!")

test_draw_shape_rectangle()
test_draw_shape_triangle()
test_draw_shape_circle()