import turtle
import colorsys
import os
from math import cos, sin, radians

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


def calc_length_height(instructions, angle, correction_angle):
    current_angle = correction_angle
    x_offset = 0
    y_offset = 0
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for inst in instructions:
        if inst == "F":
            x_offset += cos(radians(current_angle))
            y_offset += sin(radians(current_angle))
        elif inst == "B":
            x_offset -= cos(radians(current_angle))
            y_offset -= sin(radians(current_angle))
        elif inst == "+":
            current_angle -= angle
        elif inst == "-":
            current_angle += angle
        max_x = max(max_x, x_offset)
        min_x = min(min_x, x_offset)
        max_y = max(max_y, y_offset)
        min_y = min(min_y, y_offset)
    
    width = abs(max_x) + abs(min_x)
    height = abs(max_y) + abs(min_y)


    return width, height, abs(min_x), abs(min_y)

def main(iterations, axiom, rules, angle, length=None, size=None, correction_angle=0,
        y_offset=None, x_offset=None, offset_angle=None, inverted=False, flip_h=False, flip_v=False,
        color=False, filename=None, width=None, height=None, margin=None, aspect_ratio=None):

    inst = create_l_system(iterations, axiom, rules)

    width_, height_, min_x, min_y = calc_length_height(inst, angle, correction_angle)    

    if aspect_ratio is None:
        if 0 in [width_, height_]:
            aspect_ratio = 1
        else:
            aspect_ratio = width_ / height_

    if width is None and height:
        width = height / aspect_ratio

    if height is None and width:
        height = width / aspect_ratio
    
    if margin is None:
        margin = 35

    if offset_angle is None:
        offset_angle = -90

    if length is None:
        if width_ > height_:
            length = (width - 2 * margin) / width_
        else:
            length = (height - 2 * margin) / height_
    
    if width_ * length > width:
        length = (width - 2 * margin) / width_
    elif height_ * length > height:
        length = (height - 2 * margin) / height_
    
    if x_offset is None:
        if width_ >= height_  and (width - width_) <= width_ - 2 * margin :
            x_offset = -(width / 2 - margin) + min_x * length
        else:
            x_offset = -(width / 2) + (width - width_ * length) / 2 + min_x * length
    
    if y_offset is None:
        if height_ >= width_ and (height - height_) <= height_ - 2 * margin :
            y_offset = -(height / 2 - margin) + min_y * length
        else:
            y_offset = -(height / 2) + (height - height_ * length) / 2 + min_y * length


    if inverted:
        inst = inst.replace('+', '$')
        inst = inst.replace('-', '+')
        inst = inst.replace('$', '-')
        inst = inst.replace('F', '$')
        inst = inst.replace('B', 'F')
        inst = inst.replace('$', 'B')
    
    if flip_h:
        inst = inst.replace('F', '$')
        inst = inst.replace('B', 'F')
        inst = inst.replace('$', 'B')
        y_offset = -y_offset

    if flip_v:
        inst = inst.replace('+', '$')
        inst = inst.replace('-', '+')
        inst = inst.replace('$', '-')
        y_offset = -y_offset

    print(f"Width: {width_} - Height:{height_ }")

    print(length)

    if size is None:
        if length < 2:
            size = 1
        else:
            size = 2

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
iterations = 1
angle = 90
width = 500

# main(iterations, axiom, rules, angle, color=True, width=width) # ,  filename=title.replace(" ","-"))

# box fractal
title = "box fractal"
axiom = "F-F-F-F"
rules = {"F":"F-F+F+F-F"}
iterations = 2
angle = 90
width = 450

# main(iterations, axiom, rules, angle, color=True, width=width) # ,  filename=title.replace(" ","-"))

# Dragon curve
title = "Dragon curve"
axiom = "FX"
rules = {"X":"X+YF+", "Y":"-FX-Y"}
iterations = 0
angle = 90
width = 500

# main(iterations, axiom, rules, angle, color=True, width=width) # ,  filename=title.replace(" ","-"))

# 2 2 4 4 8 10 18 20 36 42 74 84 148

# Hilbert curve
title = "Hilbert curve"
axiom = "L"
rules = {"L":"+RF-LFL-FR+", "R":"-LF+RFR+FL-"}
iterations = 3
angle = 90
width = 450
y_offset = -190
angle_offset = 90

# main(iterations, axiom, rules, angle, color=True, width=width, inverted=True,
#         offset_angle=angle_offset, y_offset=y_offset) # ,  filename=title.replace(" ","-"))

# Hilbert curve II
title = "Hilbert curve II"
axiom = "X"
rules = {"X":"XFYFX+F+YFXFY-F-XFYFX", "Y":"YFXFY-F-XFYFX+F+YFXFY"}
iterations = 4
angle = 90
width = 450
y_offset = -190
angle_offset = 0

# main(iterations, axiom, rules, angle, color=True, width=width, 
#           offset_angle=angle_offset, y_offset=y_offset) # ,  filename=title.replace(" ","-"))


# 2 8 26 80 242 728

# Koch snowflake
title = "Koch snowflake"
axiom = "F--F--F"
rules = {"F":"F+F--F+F"}
iterations = 0
angle = 60
width = 450

# main(iterations, axiom, rules, angle, color=True, width=width) # ,  filename=title.replace(" ","-"))

# 1 3 9 27 81 243 729

# Peano curve
title = "Peano curve"
axiom = "F"
rules = {"F":"F+F-F-F-F+F+F+F-F"}
iterations = 2
angle = 90
width = 450

# main(iterations, axiom, rules, angle, color=True, width=width) # ,  filename=title.replace(" ","-"))

# 1 3 9 27 81 243 729

# Peano-Gosper curve
title = "Peano-Gosper curve"
axiom = "FX"
rules = {"X":"X+YF++YF-FX--FXFX-YF+", "Y":"-FX+YFYF++YF+FX--FX-Y"}
iterations = 4
angle = 60
width = 450

# main(iterations, axiom, rules, angle, color=True, width=width) # ,  filename=title.replace(" ","-"))

# ? 2.5 7 20 55 150

# quadratic Koch island
title = "quadratic Koch island"
axiom = "F+F+F+F"
rules = {"F":"F-F+F+FFF-F-F+F"}
iterations = 2
angle = 90
width = 450
height = 450
x_offset = -65
y_offset = 145
angle_offset = -90+20

# main(iterations, axiom, rules, angle, color=True, width=width) # ,  filename=title.replace(" ","-"))

# 1 7 31 127

# Sierpiński arrowhead
title = "Sierpiński arrowhead"
axiom = "YF"
rules = {"X":"YF+XF+Y", "Y":"XF-YF-X"}
iterations = 1
angle = 60
width = 450
aspect_ratio = 9 / 8
margin = 35
length = (width - 2 * margin) / 2**(iterations+1)
y_offset = -150
x_offset = 190
angle_offset = 90
correction_angle = 0 if iterations % 2 == 0 else -60
offset_angle = -90 if iterations % 2 == 0 else -30
flip_v = iterations % 2 == 0

# main(iterations, axiom, rules, angle, flip_v=True, 
#         correction_angle=correction_angle, offset_angle=offset_angle, color=True, width=width, height=width) # ,  filename=title.replace(" ","-"))

# Sierpiński curve
title = "Sierpiński curve"
axiom = "F+XF+F+XF"
rules = {"X":"XF-F+F-XF+F+XF-F+F-X"}
iterations = 4
angle = 90
width = 450

# main(iterations, axiom, rules, angle, color=True, width=width) # ,  filename=title.replace(" ","-"))

# Siepiński sieve
title = "Siepiński sieve"
axiom = "FXF--FF--FF"
rules = {"F":"FF", "X":"--FXF++FXF++FXF--"}
iterations = 2
angle = 60
width = 450
aspect_ratio = 8 / 9
margin = 35
length = (width - 2 * margin) / 2 ** (iterations + 1 )
angle_offset = -90

# main(iterations, axiom, rules, angle, color=True, width=width) # ,  filename=title.replace(" ","-"))
