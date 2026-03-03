from turtle import Screen,Turtle
import tkinter, random
colors = [
    "red",          # Classic bright red
    "deep sky blue", # A vibrant, modern blue
    "chartreuse",   # A bright neon lime-green
    "orange",       # Standard orange
    "hot pink",     # Very bright pink
    "gold",         # A rich yellow-gold
    "dark orchid",  # A deep, royal purple
    "aquamarine",   # A soft sea-foam blue/green
    "firebrick",    # A sophisticated dark red
    "slate gray"    # A cool, professional gray
]
tam = Turtle()
tam_Screen = Screen()
tam_Screen.listen()


tam.shape("arrow")
tam.pensize(2)

line_len = 100
line_count = 3

while line_count <= 10:
    random_color = random.choice(colors)
    colors.remove(random_color)
    tam.pencolor(random_color)
    for _ in range(line_count):
        tam.fd(line_len)
        tam.right(360/line_count)
    line_count += 1


tam_Screen.exitonclick()
