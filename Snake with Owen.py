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


