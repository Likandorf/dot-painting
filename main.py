from turtle import Turtle, Screen
import random

color_list = [(198, 162, 101), (63, 90, 126), (139, 170, 191), (136, 91, 50), (132, 28, 53), (219, 205, 120),
              (29, 40, 65), (78, 16, 35), (149, 62, 85), (162, 155, 53), (184, 141, 158), (132, 182, 145),
              (48, 56, 99), (180, 97, 107), (56, 35, 22), (68, 130, 106), (98, 118, 166), (82, 148, 159),
              (221, 175, 187), (169, 206, 166), (90, 151, 96), (185, 97, 80), (163, 200, 213), (179, 188, 211),
              (80, 70, 39), (131, 37, 27)]

screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.shape("turtle")
up = 0
tim.penup()
for _ in range(10):
    tim.goto(-200, up)
    for _ in range(10):
        tim.pencolor(random.choice(color_list))
        tim.dot(10)
        tim.forward(25)
    up += 30


screen.exitonclick()
