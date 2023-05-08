import turtle
import time
import random

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width = 600, height = 600)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)

# Food code
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)



while True:
    window.update()

    time.sleep(0.1)