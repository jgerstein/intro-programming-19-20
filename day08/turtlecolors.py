import turtle as t

digits = '0123456789abcdef'
rev_digits = digits[::-1]

z = zip(rev_digits, digits)

spectrum = []

#red-green
for r, g in zip(rev_digits, digits):
    spectrum.append(f"#{r}{r}{g}{g}00")
    
#green-blue
for g, b in zip(rev_digits, digits):
    spectrum.append(f"#00{g}{g}{b}{b}")

#blue-red
for b, r in zip(rev_digits, digits):
    spectrum.append(f"#{r}{r}00{b}{b}")


print(spectrum)
t.speed(0)
t.hideturtle()
t.pensize(3)
while True:
    for c in spectrum:
        t.color(c)
        t.fd(150)
        t.rt(180-11)

print(len(spectrum))

t.mainloop()