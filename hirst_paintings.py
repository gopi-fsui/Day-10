import random
import turtle as t

# import colorgram

# colors = colorgram.extract('Img.jpg',31)
# print(colors)
# print(len(colors))
# rgb_colors = []

# for color in colors:
#     rgb_colors.append((color.rgb[0],color.rgb[1],color.rgb[2]))
#     # or rgb_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))

# del rgb_colors[0]
# print(rgb_colors)
# print(len(rgb_colors))
color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42)]

tam = t.Turtle()
tam_Screen = t.Screen()
t.colormode(255)
tam_Screen.listen()
tam.shape("arrow")
tam.pensize(1)
tam.speed("fastest")
tam.penup()
tam.hideturtle()

def draw_paintings(x,y,dot_size,gap_width):

    x_axis = -((x-1) * gap_width)/2
    y_axis = -((y-1) * gap_width)/2
    tam.teleport(x_axis,y_axis)
    for numy in range(y):
        for numx in range(x):
            tam.dot(dot_size, random.choice(color_list))
            if not numx == x-1 :
             tam.fd(gap_width)
        if not numy == y-1 :
            tam.teleport(x_axis, None)
            tam.left(90)
            tam.fd(gap_width)
            tam.right(90)

draw_paintings(18,15,50,100)
tam_Screen.mainloop()



