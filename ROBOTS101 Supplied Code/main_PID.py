from time import sleep
import turtle
import PID

window = turtle.Screen()
window.bgcolor("blue")
window.title("PID Controller Demo")
window.listen()

character = turtle.Turtle()
character.shape("turtle")
character.color("white")
character.penup()
character.goto(-100, 0)
character.speed(0)
character.velocity = 0
character.power = 1
character.left(90)

marker = turtle.Turtle()
marker.shape("square")
marker.color("red")
marker.penup()
marker.goto(0, 50)
marker.speed(0)

controller = PID.PID(2, 0, 0.3, 1, -1)

timeStep = 0.01
target = 0

def setOne():
    global target
    target = -400

def setTwo():
    global target
    target = -200

def setThree():
    global target
    target = 0

def setFour():
    global target
    target = 200

def setFive():
    global target
    target = 400



window.onkeypress(setOne, "1")
window.onkeypress(setTwo, "2")
window.onkeypress(setThree, "3")
window.onkeypress(setFour, "4")
window.onkeypress(setFive, "5")

while True:
    throttle = controller.update(target, character.xcor(), timeStep)
    character.velocity += throttle * character.power
    character.setx(character.xcor() + character.velocity)
    marker.setx(target)
    window.update()
    sleep(timeStep)