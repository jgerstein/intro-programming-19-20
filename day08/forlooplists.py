import turtle as t


colors = ["red", "orangered", "darkorange", "orange", "gold", "yellow", "greenyellow", "lime", "limegreen", "green", "teal", "darkturquoise", "deepskyblue", "dodgerblue", "blue", "darkblue", "indigo", "purple", "fuchsia", "deeppink"]

turtles = [t.Turtle() for c in colors]

for n in range(len(colors)):
    turtles[n].speed(0)
    turtles[n].color(colors[n])
    turtles[n].rt(360/len(colors) * n)
    turtles[n].pensize(5)

for n in range(300):
    for trtl in turtles:
        trtl.fd(n)
        trtl.rt(15)
    


t.mainloop()