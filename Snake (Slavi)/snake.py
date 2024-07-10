import turtle
import time
import random
import pygame
import tkinter as tk
from tkinter import messagebox

delay = 0.15
score = 0
high_score = 0

# Initialize pygame and the mixer
pygame.init()
pygame.mixer.init()

# Load the background music
pygame.mixer.music.load("C:\\Users\\user.DESKTOP-LOCT6MV\Documents\Snake (Slavi)\\music.wav")
pygame.mixer.music.play(-1)
# Play the music in a loop

# Load the eat food sound effect
eat_sound = pygame.mixer.Sound("C:\\Users\\user.DESKTOP-LOCT6MV\\Documents\\Snake (Slavi)\\eatfood.wav")

# Set up the screen
win = turtle.Screen()
win.title("Snake game")
win.bgcolor("#0a7001")
win.setup(width=600, height=600)
win.tracer(0)
# Turns off the screen updates

# Prevent window resizing
root = win._root
root.resizable(False, False)

# Set the icon for the window
icon_path = "C:\\Users\\user.DESKTOP-LOCT6MV\\Documents\\Snake (Slavi)\\icon.ico"
root.iconbitmap(icon_path)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("#02eb48")
head.penup()
head.shapesize(1.5, 1.5)
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(1, 1)
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-290, 243)
pen.write("Welcome to my game!\n", align="left", font=("Segoe UI", 15, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def end_game():
    global score, high_score, segments, delay
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

    if score > high_score:
        high_score = score

    score = 0
    delay = 0.15
    pen.clear()
    pen.write("Current score:  {}\nBest score:  {}".format(score, high_score), align="left", font=("Segoe UI", 15, "normal"))

    show_end_screen()

def show_end_screen():
    root = tk.Tk()
    root.withdraw()
    result = messagebox.askyesno("You died!", "Do you want to play again?")
    if result:
        root.destroy()
    else:
        win.bye()
        root.destroy()

# Keyboard bindings
win.listen()
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_left, "Left")
win.onkey(go_right, "Right")

# Main game loop
while True:
    win.update()

    # Check for a collision with the border
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)
    if head.ycor() < -290:
        head.sety(290)

    # Check for a collision with the food
    if head.distance(food) < 20:
        eat_sound.play()

        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#02d642")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.002
        score += 1

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Current score:  {}\nBest score:  {}".format(score, high_score), align="left", font=("Segoe UI", 15, "normal"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            end_game()

    time.sleep(delay)

win.mainloop()
