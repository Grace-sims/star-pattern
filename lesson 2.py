import turtle as t

y = input("what is the color of a star?")
d = input("what is the color of the background?")
w = int(input("wth is the width?"))
s = int(input("what is the size of the star"))

t.bgcolor (d)

t.color (y)

t.width (w)

for x in range (5):
    t.forward(s)
    t.right(144)

t.mainloop ()