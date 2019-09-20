import turtle as t

sides = int(input("how many sides for your polygon? "))

t.pensize(5)
t.speed(0)
t.hideturtle()

colors = ["red", "orangered", "darkorange", "orange", "gold", "yellow", "greenyellow", "lime", "limegreen", "green", "teal", "darkturquoise", "deepskyblue", "dodgerblue", "blue", "darkblue", "indigo", "purple", "fuchsia", "deeppink"]

t.color('purple')

if sides == 3:
    for n in range(3):
        t.fd(100)
        t.rt(120)

elif sides == 4:
    for n in range(4):
        t.fd(100)
        t.rt(90)

elif sides == 6:
    for n in range(6):
        t.fd(100)
        t.rt(150)

else:
    print("I don't feel like writing more options so you get a circle")
    for n in range(360):
        t.color(colors[n%len(colors)])
        t.fd(2)
        t.rt(1)

t.mainloop()