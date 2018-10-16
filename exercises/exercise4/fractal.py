import turtle
import colorsys
import os

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string


def draw_l_system(aTurtle, wn, instructions, angle, distance, color):
    steps = len([i for i in instructions if i in "FB"])
    step = 1 / steps
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

def draw_background(t):
    """ Draw a background rectangle. """
    ts = t.getscreen()
    canvas = ts.getcanvas()
    height = ts.getcanvas()._canvas.winfo_height()
    width = ts.getcanvas()._canvas.winfo_width()

    turtleheading = t.heading()
    turtlespeed = t.speed()
    penposn = t.position()
    penstate = t.pen()

    t.penup()
    t.speed(0)  # fastest
    t.goto(-width/2-2, -height/2+3)
    t.fillcolor(turtle.Screen().bgcolor())
    t.begin_fill()
    t.setheading(0)
    t.forward(width)
    t.setheading(90)
    t.forward(height)
    t.setheading(180)
    t.forward(width)
    t.setheading(270)
    t.forward(height)
    t.end_fill()

    t.penup()
    t.setposition(*penposn)
    t.pen(penstate)
    t.setheading(turtleheading)
    t.speed(turtlespeed)


def main(iterations, axiom, rules, angle, length, size=2,
        y_offset=None, x_offset=None, offset_angle=0, 
        color=False, filename=None, width=None, height=None, margin=35, aspect_ratio=1):

    if width is None and height:
        width = aspect_ratio / height

    if height is None and width:
        height = aspect_ratio * width

    if x_offset is None:
        x_offset = -(width / 2 - margin)
    
    if y_offset is None:
        y_offset = -(height / 2 - margin)

    inst = create_l_system(iterations, axiom, rules)

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    if color:
        wn.bgcolor('black')

    if not filename is None:
        draw_background(t)        

    t.up()    
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, wn, inst, angle, length, color)
    t.hideturtle()
    
    if not filename is None:
        if not os.path.exists(filename):
            os.makedirs(filename)
        cv = wn.getcanvas()
        cv.postscript(file=f"{filename}\{filename}_{iterations}.ps", colormode='color')
        try: # Needs Image Magick Convert
            command = f"convert -density 1000 -resize {width}x{height} -flatten -background black -units pixelsperinch {filename}\{filename}_{iterations}.ps {filename}\{filename}_{iterations}.png"
            print(command)
            os.system(command)
        except:
            pass
        
    wn.exitonclick()


# 32-segment curve
title = "32-segment curve"
axiom = "F+F+F+F"
rules = {"F":"-F+F-F-F+F+FF-F+F+FF+F-F-FF+FF-FF+F+F-FF-F-F+FF-F-F+F+F-F+"}
iterations = 2
angle = 90
width = 450
height = 450
margin = 35
length = (width - 2 * margin ) / 135
x_offset = -32*length
y_offset = 190-36*length
angle_offset = -90

# 1 16 135 

# box fractal
title = "box fractal"
axiom = "F-F-F-F"
rules = {"F":"F-F+F+F-F"}
iterations = 6
angle = 90
width = 450
margin = 35
length = (width - 2 * margin) / 3 ** (iterations)
angle_offset = -90

# 1 3 9 

# Dragon curve
title = "Dragon curve"
axiom = "FX"
rules = {"X":"X+YF+", "Y":"-FX-Y"}
iterations = 12
angle = 90
width = 450
height = 450
margin = 35
length = (width - 2 * margin) / (2 * 74)
x_offset = 0
y_offset = 0
angle_offset = -90

# 2 2 4 4 8 10 18 20 36 42 74 84 148

# Dragon curve
title = "Dragon curve v 2"
axiom = "FX"
rules = {"X":"X+YF+", "Y":"-FX-Y"}
iterations = 0
angle = 90
width = 450
height = 450
margin = 35
length = (width - 2 * margin) / (95)
x_offset =  width / 2 - margin - 21 * length#
y_offset = (width / 2) - ( (width - 63 * length) / 2 + 21 * length)
angle_offset = -90

# 2 2 4 4 5 7 15 15 24 31 47 62 95


main(iterations, axiom, rules, angle, size=2, x_offset=x_offset, y_offset=y_offset,
    length=length, offset_angle=angle_offset,  
    color=True, width=width, height=height,  filename=title.replace(" ","-"))

# Hilbert curve
title = "Hilbert curve"
axiom = "L"
rules = {"L":"+RF-LFL-FR+", "R":"-LF+RFR+FL-"}
iterations = 9
angle = 90
width = 450
height = 450
x_offset = -190
y_offset = -190 
angle_offset = 0

# Hilbert curve II
title = "Hilbert curve II"
axiom = "X"
rules = {"X":"XFYFX+F+YFXFY-F-XFYFX", "Y":"YFXFY-F-XFYFX+F+YFXFY"}
iterations = 6
angle = 90
width = 450
height = 450
x_offset = -190
y_offset = -190
angle_offset = 0

# 2 8 26 80 242 728

# Koch snowflake
title = "Koch snowflake"
axiom = "F--F--F"
rules = {"F":"F+F--F+F"}
iterations = 6
angle = 60
width = 450
height = 500
x_offset = -190
y_offset = -235+380/3
angle_offset = -90

# 1 3 9 27 81 243 729

# Peano curve
title = "Peano curve"
axiom = "F"
rules = {"F":"F+F-F-F-F+F+F+F-F"}
iterations = 6
angle = 90
width = 450
height = 450
x_offset = -190
y_offset = 0
angle_offset = -90

# 1 3 9 27 81 243 729

# Peano-Gosper curve
title = "Peano-Gosper curve"
axiom = "FX"
rules = {"X":"X+YF++YF-FX--FXFX-YF+", "Y":"-FX+YFYF++YF+FX--FX-Y"}
iterations = 5
angle = 60
width = 450
height = 450
x_offset = -30
y_offset = 190 
angle_offset = -90+30+15

# ? 2.5 7 20 55 150

# quadratic Koch island
title = "quadratic Koch island"
axiom = "F+F+F+F"
rules = {"F":"F-F+F+FFF-F-F+F"}
iterations = 3
angle = 90
width = 450
height = 450
x_offset = -65
y_offset = 145
angle_offset = -90+20


# 1 7 31 127

# Sierpiński arrowhead
title = "Sierpiński arrowhead"
axiom = "YF"
rules = {"X":"YF+XF+Y", "Y":"XF-YF-X"}
iterations = 2
angle = 60
width = 450
aspect_ratio = 9 / 8
margin = 35
length = (width - 2 * margin) / 2**(iterations+1)
y_offset = -150
x_offset = 190
angle_offset = 90

# Sierpiński curve
title = "Sierpiński curve"
axiom = "F+XF+F+XF"
rules = {"X":"XF-F+F-XF+F+XF-F+F-X"}
iterations = 8
angle = 90
width = 450
margin = 35
length = (width - 2 * margin) / (2 ** (iterations+2) - 3)
x_offset = -length*0.5
y_offset = (width - 2 * margin) /2
angle_offset = -90

# Siepiński sieve
title = "Siepiński sieve"
axiom = "FXF--FF--FF"
rules = {"F":"FF", "X":"--FXF++FXF++FXF--"}
iterations = 7
angle = 60
width = 450
aspect_ratio = 8 / 9
margin = 35
length = (width - 2 * margin) / 2 ** (iterations + 1 )
angle_offset = -90
