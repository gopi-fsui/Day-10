from turtle import Screen,Turtle


tam = Turtle()
tam_Screen = Screen()


tam.shape("arrow")

tam.pensize(2)

for k in range(50):
    tam.fd(10)
    tam.up()
    tam.fd(10)
    tam.pd()





tam_Screen.listen()
tam_Screen.exitonclick()
