import turtle as t
import random

tam = t.Turtle()
tam_Screen = t.Screen()
t.colormode(255)
tam_Screen.listen()
tam.shape("arrow")
tam.pensize(1)
tam.speed("fastest")
is_running = True

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b
  
def spirograph(gap_size):
    for x in range(0, 360, gap_size):
        tam.pencolor(random_color())
        tam.setheading(x)
        tam.circle(250)

spirograph(5)
tam.teleport(-500,500)
tam.hideturtle()
tam.write("Finished",font=("",30,"bold"))

tam_Screen.mainloop()
