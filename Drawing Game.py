# Drawing Game
# Hayden Fee
# 6/7/2022
import turtle


def right():
    player.right(15)


def left():
    player.left(15)


def forward():
    player.forward(pdistance["val"])

    p1.penup()
    p1.goto(600, 400)
    p1.pendown()
    p1.write("Distance = " + str(pdistance["val"]), font=style)
    p1.penup()
    p1.goto(600, 300)
    p1.pendown()
    p1.write("Colour = " + colors[pcolor["val"]], font=style)
    p1.penup()
    p1.goto(600, 200)
    p1.pendown()
    p1.write("Width = " + str(pwidth["val"]), font=style)


def forwardcolor():
    pcolor["val"] += 1
    if pcolor["val"] > len(colors) - 1:
        pcolor["val"] = 0
    player.color(colors[pcolor["val"]])

    p1.clear()
    p1.penup()
    p1.goto(600, 400)
    p1.pendown()
    p1.write("Distance = " + str(pdistance["val"]), font=style)
    p1.penup()
    p1.goto(600, 300)
    p1.pendown()
    p1.write("Colour = " + colors[pcolor["val"]], font=style)
    p1.penup()
    p1.penup()
    p1.goto(600, 200)
    p1.pendown()
    p1.write("Width = " + str(pwidth["val"]), font=style)


def backwardcolor():
    pcolor["val"] -= 1
    if pcolor["val"] < 0:
        pcolor["val"] = len(colors) - 1
    player.color(colors[pcolor["val"]])

    p1.clear()
    p1.penup()
    p1.goto(600, 400)
    p1.pendown()
    p1.write("Distance = " + str(pdistance["val"]), font=style)
    p1.penup()
    p1.goto(600, 300)
    p1.pendown()
    p1.write("Colour = " + colors[pcolor["val"]], font=style)
    p1.penup()
    p1.penup()
    p1.goto(600, 200)
    p1.pendown()
    p1.write("Width = " + str(pwidth["val"]), font=style)


def clear():
    player.clear()


def distanceup():
    pdistance["val"] += 10

    p1.clear()
    p1.penup()
    p1.goto(600, 400)
    p1.pendown()
    p1.write("Distance = " + str(pdistance["val"]), font=style)
    p1.penup()
    p1.goto(600, 300)
    p1.pendown()
    p1.write("Colour = " + colors[pcolor["val"]], font=style)
    p1.penup()
    p1.goto(600, 200)
    p1.pendown()
    p1.write("Width = " + str(pwidth["val"]), font=style)


def distancedown():
    pdistance["val"] -= 10

    p1.clear()
    p1.penup()
    p1.goto(600, 400)
    p1.pendown()
    p1.write("Distance = " + str(pdistance["val"]), font=style)
    p1.penup()
    p1.goto(600, 300)
    p1.pendown()
    p1.write("Colour = " + colors[pcolor["val"]], font=style)
    p1.penup()
    p1.goto(600, 200)
    p1.pendown()
    p1.write("Width = " + str(pwidth["val"]), font=style)


def widthup():
    pwidth["val"] += 5
    player.width(pwidth["val"])

    p1.clear()
    p1.penup()
    p1.goto(600, 400)
    p1.pendown()
    p1.write("Distance = " + str(pdistance["val"]), font=style)
    p1.penup()
    p1.goto(600, 300)
    p1.pendown()
    p1.write("Colour = " + colors[pcolor["val"]], font=style)
    p1.penup()
    p1.goto(600, 200)
    p1.pendown()
    p1.write("Width = " + str(pwidth["val"]), font=style)


def widthdown():
    pwidth["val"] -= 5
    if pwidth["val"] < 0:
        pwidth["val"] = 0
    player.width(pwidth["val"])

    p1.clear()
    p1.penup()
    p1.goto(600, 400)
    p1.pendown()
    p1.write("Distance = " + str(pdistance["val"]), font=style)
    p1.penup()
    p1.goto(600, 300)
    p1.pendown()
    p1.write("Colour = " + colors[pcolor["val"]], font=style)
    p1.penup()
    p1.goto(600, 200)
    p1.pendown()
    p1.write("Width = " + str(pwidth["val"]), font=style)


def reset():
    player.penup()
    player.goto(0, 0)
    player.pendown()


pwidth = {
    "val": 10
}
pdistance = {
    "val": 15
}
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
pcolor = {
    "val": 0
}
style = ("arial", 20)

wn = turtle.Screen()
wn.title("Thng")
wn.bgcolor("#ffffff")
wn.setup(1920, 1080)

p1 = turtle.Turtle()
p1.hideturtle()
p1.speed(0)
p1.color("black")

p1.clear()
p1.penup()
p1.goto(600, 400)
p1.pendown()
p1.write("Distance = " + str(pdistance["val"]), font=style)
p1.penup()
p1.goto(600, 300)
p1.pendown()
p1.write("Colour = " + colors[pcolor["val"]], font=style)
p1.penup()
p1.goto(600, 200)
p1.pendown()
p1.write("Width = " + str(pwidth["val"]), font=style)

p1.penup()
p1.goto(-800, 400)
p1.pendown()
p1.write("controls: wad, q/e, arrow keys, r, spacebar", font=style)

player = turtle.Turtle()
player.width(10)
player.color(colors[pcolor["val"]])
player.shape("triangle")

wn.onkey(right, "d")
wn.onkey(left, "a")
wn.onkey(forward, "w")
wn.onkey(forwardcolor, "e")
wn.onkey(backwardcolor, "q")
wn.onkey(clear, "space")
wn.onkey(distanceup, "Up")
wn.onkey(distancedown, "Down")
wn.onkey(widthdown, "Left")
wn.onkey(widthup, "Right")
wn.onkey(reset, "r")

wn.listen()
wn.mainloop()
