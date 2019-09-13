# import turtle library
import turtle as t

colors = ["red", "orangered", "darkorange", "orange", "gold", "yellow", "greenyellow", "lime", "limegreen", "green", "teal", "darkturquoise", "deepskyblue", "dodgerblue", "blue", "darkblue", "indigo", "purple", "fuchsia", "deeppink"]

# t.pensize(5)

def star(sz):
    # t.begin_fill()
    for n in range(5):
        t.fd(sz)
        t.rt(144)
    # t.end_fill()

for n in colors:
    t.pencolor(n)
    star(200)
    t.rt(360/len(colors))

t.mainloop()



# for n in range(500):
#     t.color(colors[n%len(colors)])
#     t.fd(n)
#     t.rt(50)