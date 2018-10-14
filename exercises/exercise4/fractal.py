import turtle
import colorsys

def create_l_system(numIters, axiom):
    startString = axiom
    endString = ""
    for _ in range(numIters):
        endString = "".join(rules[i] if i in rules else i for i in startString)
        startString = endString

    return endString


def draw_l_system(aTurtle, instructions, angle, distance, color):
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

def main(iterations, axiom, angle, length, y_offset=0, x_offset=0, offset_angle=0, color=False):
    inst = create_l_system(iterations, axiom)

    t = turtle.Turtle()
    wn = turtle.Screen()


    if color:
        wn.bgcolor('black')

    t.up()    
    t.backward(-x_offset)
    t.right(270)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    draw_l_system(t, inst, angle, length, color)
    t.hideturtle()
    
    wn.exitonclick()


# 32-segment curve
title = "32-segment curve"
axiom = "F+F+F+F"
rules = {"F":"-F+F-F-F+F+FF-F+F+FF+F-F-FF+FF-FF+F+F-FF-F-F+FF-F-F+F+F-F+"}
iterations = 2
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
iterations = 6
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
iterations = 3
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
iterations = 2
angle = 90

# Sierpiński arrowhead
title = "Sierpiński arrowhead"
axiom = "YF"
rules = {"X":"YF+XF+Y", "Y":"XF-YF-X"}
iterations = 6
angle = 60

# Sierpiński curve
title = "Sierpiński curve"
axiom = "F+XF+F+XF"
rules = {"X":"XF-F+F-XF+F+XF-F+F-X"}
iterations = 3
angle = 90

# Siepiński sieve
title = "Siepiński sieve"
axiom = "FXF--FF--FF"
rules = {"F":"FF", "X":"--FXF++FXF++FXF--"}
iterations = 4
angle = 60

main(iterations, axiom, angle, length=8, y_offset=0, x_offset=-300, offset_angle=-90)