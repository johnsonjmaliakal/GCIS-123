import turtle
def drawSquare(d):
    x = turtle.isdown()
    if x == True:
        pass
    else:
        turtle.down()
    for i in range (4):
        turtle.forward(d)
        turtle.left(90)
    turtleX = int(turtle.xcor())
    turtleY = int(turtle.ycor())
    print("Square has been printed\n", turtleX, turtleY)
    input("Press Enter to continue: ")

#drawSquare()

def drawPattern(distance, angle):
    x = turtle.isdown()
    if x == True:
        pass
    else:
        turtle.down()
    initX = int(turtle.xcor())
    initY = int(turtle.ycor())
    counter = 0
  
    while True and counter <= 100:
        counter += 1
        
        turtle.forward(distance)
        turtle.right(angle)
        turtleX = int(turtle.xcor())
        turtleY = int(turtle.ycor())
        if turtleX == initX and turtleY == initY:
            break
        else:
            turtle.forward(distance)
            turtle.right(angle)
            
    print("Pattern has been printed")
    input("Press Enter to continue: ")

#d = int(input("Enter distance of pattern: "))
#a = int(input("Enter angle or pattern: "))
#drawPattern(d, a)

def testPattern():
    turtle.bgcolor("black")
    colors = [
        #reddish colors
        (1.00, 0.00, 0.00),(1.00, 0.03, 0.00),(1.00, 0.05, 0.00),(1.00, 0.07, 0.00),(1.00, 0.10, 0.00),(1.00, 0.12, 0.00),(1.00, 0.15, 0.00),(1.00, 0.17, 0.00),(1.00, 0.20, 0.00),(1.00, 0.23, 0.00),(1.00, 0.25, 0.00),(1.00, 0.28, 0.00),(1.00, 0.30, 0.00),(1.00, 0.33, 0.00),(1.00, 0.35, 0.00),(1.00, 0.38, 0.00),(1.00, 0.40, 0.00),(1.00, 0.42, 0.00),(1.00, 0.45, 0.00),(1.00, 0.47, 0.00),
        #orangey colors
        (1.00, 0.50, 0.00),(1.00, 0.53, 0.00),(1.00, 0.55, 0.00),(1.00, 0.57, 0.00),(1.00, 0.60, 0.00),(1.00, 0.62, 0.00),(1.00, 0.65, 0.00),(1.00, 0.68, 0.00),(1.00, 0.70, 0.00),(1.00, 0.72, 0.00),(1.00, 0.75, 0.00),(1.00, 0.78, 0.00),(1.00, 0.80, 0.00),(1.00, 0.82, 0.00),(1.00, 0.85, 0.00),(1.00, 0.88, 0.00),(1.00, 0.90, 0.00),(1.00, 0.93, 0.00),(1.00, 0.95, 0.00),(1.00, 0.97, 0.00),
        #yellowy colors
        (1.00, 1.00, 0.00),(0.95, 1.00, 0.00),(0.90, 1.00, 0.00),(0.85, 1.00, 0.00),(0.80, 1.00, 0.00),(0.75, 1.00, 0.00),(0.70, 1.00, 0.00),(0.65, 1.00, 0.00),(0.60, 1.00, 0.00),(0.55, 1.00, 0.00),(0.50, 1.00, 0.00),(0.45, 1.00, 0.00),(0.40, 1.00, 0.00),(0.35, 1.00, 0.00),(0.30, 1.00, 0.00),(0.25, 1.00, 0.00),(0.20, 1.00, 0.00),(0.15, 1.00, 0.00),(0.10, 1.00, 0.00),(0.05, 1.00, 0.00),
        #greenish colors
        (0.00, 1.00, 0.00),(0.00, 0.95, 0.05),(0.00, 0.90, 0.10),(0.00, 0.85, 0.15),(0.00, 0.80, 0.20),(0.00, 0.75, 0.25),(0.00, 0.70, 0.30),(0.00, 0.65, 0.35),(0.00, 0.60, 0.40),(0.00, 0.55, 0.45),(0.00, 0.50, 0.50),(0.00, 0.45, 0.55),(0.00, 0.40, 0.60),(0.00, 0.35, 0.65),(0.00, 0.30, 0.70),(0.00, 0.25, 0.75),(0.00, 0.20, 0.80),(0.00, 0.15, 0.85),(0.00, 0.10, 0.90),(0.00, 0.05, 0.95),
        #blueish colors
        (0.00, 0.00, 1.00),(0.05, 0.00, 1.00),(0.10, 0.00, 1.00),(0.15, 0.00, 1.00),(0.20, 0.00, 1.00),(0.25, 0.00, 1.00),(0.30, 0.00, 1.00),(0.35, 0.00, 1.00),(0.40, 0.00, 1.00),(0.45, 0.00, 1.00),(0.50, 0.00, 1.00),(0.55, 0.00, 1.00),(0.60, 0.00, 1.00),(0.65, 0.00, 1.00),(0.70, 0.00, 1.00),(0.75, 0.00, 1.00),(0.80, 0.00, 1.00),(0.85, 0.00, 1.00),(0.90, 0.00, 1.00),(0.95, 0.00, 1.00)
        ]
    speed = 1
    for i in range(1000):
        speed+=20000
        turtle.speed(speed)
        idx = int(i/10)
        color = colors[idx]
        turtle.color(color)
        turtle.forward(i)
        turtle.right(98)
    input("enter")
testPattern()
import math
def circleSquare():
    r = int(input("Enter Radius of circle: "))
    turtle.circle(r)
    rootTwo = math.sqrt(2)
    d = rootTwo*r
    h = turtle.heading()
    turtle.left(45)
    drawSquare(d)
    turtle.setheading(h)
    turtle.up()
    turtle.circle(r, 30)
    h = turtle.heading()
    turtle.down()
    turtle.left(45)
    drawSquare(d)
    turtle.setheading(h)
    turtle.up()
    turtle.circle(r, 30)
    h = turtle.heading()
    turtle.down()
    turtle.left(45)
    drawSquare(d)
    turtle.setheading(h)
#circleSquare()

def cube(d):
    x = turtle.isdown()
    if x == True:
        pass
    else:
        turtle.down()
    turtle.setheading(90)
    drawSquare(d)
    turtle.setheading(90)
    turtle.up()
    turtle.forward(d)
    turtle.down()
    turtle.left(45)
    turtle.forward(d/2)
    turtle.left(45)
    turtle.forward(d)
    turtle.left(90)
    turtle.forward(d)
    turtle.left(45)
    turtle.forward(d/2)
    turtle.setheading(90)
    turtle.up()
    turtle.forward(d)
    turtle.left(45)
    turtle.down()
    turtle.forward(d/2)
    input("cube completed, press enter to continue: ")
#d = int(input("Enter the side of your cube: "))
#cube(d)

def turtleState():
    x = int(turtle.xcor())
    y = int(turtle.ycor())
    if turtle.isdown():
        d = "Down"
    else:
        d = "Up"
    h = turtle.heading()
    t = [x, y, d, h]
    return t

def squareCircle(d):
    drawSquare(d)
    turtle.up()
    turtle.forward(d/2)
    turtle.down()
    turtle.circle(d/2)
    input("Circle in square done. Press Enter to continue: ")

#d = int(input("Enter side of your square: "))
#squareCircle(d)


print(turtleState())