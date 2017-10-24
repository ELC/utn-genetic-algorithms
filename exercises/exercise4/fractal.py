import turtle
import colorsys

def createLSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for _ in range(numIters):
        endString = "".join(rules[i] if i in rules else i for i in startString)
        startString = endString

    return endString


def drawLsystem(aTurtle, instructions, angle, distance, color):
    step = 1 / len([i for i in instructions if i in "FB"])
    i = 0
    for cmd in instructions:
        if cmd in "FB" and color:
            r, g, b = colorsys.hsv_to_rgb(i, 1.0, 1.0)
            i += step
            aTurtle.color(r, g, b)
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)

def main(iterations, axiom, angle, length, initial_angle=0, color=False):
    inst = createLSystem(iterations, axiom)

    t = turtle.Turtle()
    wn = turtle.Screen()
    t.up()
    t.backward(0)
    t.left(90)
    t.backward(-300)
    t.right(90)
    t.left(initial_angle)
    t.down()
    t.speed(0)
    t.pensize(1)
    drawLsystem(t, inst, angle, length, color)
    t.hideturtle()

    wn.exitonclick()


# 32-segment curve
title = "32-segment curve"
axiom = "F+F+F+F"
rules = {"F":"-F+F-F-F+F+FF-F+F+FF+F-F-FF+FF-FF+F+F-FF-F-F+FF-F-F+F+F-F+"}
iterations = 1
angle = 90

# box fractal
title = "box fractal"
axiom = "F-F-F-F"
rules = {"F":"F-F+F+F-F"}
iterations = 3
angle = 90

# Dragon curve
title = "Dragon curve"
axiom = "FX"
rules = {"X":"X+YF+", "Y":"-FX-Y"}
iterations = 11
angle = 90



# Hilbert curve
title = "Hilbert curve"
axiom = "L"
rules = {"L":"+RF-LFL-FR+", "R":"-LF+RFR+FL-"}
iterations = 5
angle = 90

# Hilbert curve II
title = "Hilbert curve II"
axiom = "X"
rules = {"X":"XFYFX+F+YFXFY-F-XFYFX", "Y":"YFXFY-F-XFYFX+F+YFXFY"}
iterations = 3
angle = 90


# Koch snowflake
title = "Koch snowflake"
axiom = "F--F--F"
rules = {"F":"F+F--F+F"}
iterations = 4
angle = 60


# Peano curve
title = "Peano curve"
axiom = "F"
rules = {"F":"F+F-F-F-F+F+F+F-F"}
iterations = 3
angle = 90

# Peano-Gosper curve
title = "Peano-Gosper curve"
axiom = "FX"
rules = {"X":"X+YF++YF-FX--FXFX-YF+", "Y":"-FX+YFYF++YF+FX--FX-Y"}
iterations = 3
angle = 60



# quadratic Koch island
title = "quadratic Koch island"
axiom = "F+F+F+F"
rules = {"F":"F-F+F+FFF-F-F+F"}
iterations = 3
angle = 90

main(iterations, axiom, angle, 6)

# Sierpiński arrowhead
title = "Sierpiński arrowhead"
axiom = "YF"
rules = {"X":"YF+XF+Y", "Y":"XF-YF-X"}
iterations = 7
angle = 60

# Sierpiński curve
title = "Sierpiński curve"
axiom = "F+XF+F+XF"
rules = {"X":"XF-F+F-XF+F+XF-F+F-X"}
iterations = 4
angle = 90

# Siepiński sieve
title = "Siepiński sieve"
axiom = "FXF--FF--FF"
rules = {"F":"FF", "X":"--FXF++FXF++FXF--"}
iterations = 8
angle = 60

