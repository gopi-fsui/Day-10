from turtle import Screen, Turtle
import random

colors = [
    "red",  # Classic bright red
    "deep sky blue",  # A vibrant, modern blue
    "chartreuse",  # A bright neon lime-green
    "orange",  # Standard orange
    "hot pink",  # Very bright pink
    "gold",  # A rich yellow-gold
    "dark orchid",  # A deep, royal purple
    "aquamarine",  # A soft sea-foam blue/green
    "firebrick",  # A sophisticated dark red
    "slate gray"  # A cool, professional gray
]
tam = Turtle()
tam_Screen = Screen()
tam_Screen.listen()
tam.shape("arrow")
tam.pensize(15)
tam.speed(9)

directions = [0, 90, 180, 270]

is_running = True


def stop_loop(x, y):
    global is_running
    is_running = False
    tam.write(f"{x, y}")


tam_Screen.onscreenclick(stop_loop)

while is_running:
    tam.right(random.choice(directions))
    tam.fd(30)
    tam.pencolor(random.choice(colors))

print(tam_Screen.exitonclick())
