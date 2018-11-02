import turtle
import colorsys
import json

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string


def draw_l_system(t, instructions, angle, distance, color):
    steps = len([i for i in instructions if i == "F"])
    step = 1 / steps
    i = 0
    for cmd in instructions:        
        if cmd == 'F':
            if color:
                r, g, b = colorsys.hsv_to_rgb(i, 1.0, 1.0)
                i += step
                t.color(r, g, b)
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)


def main(iterations, axiom, rules, angle, length=8, color=True, size=2, 
        y_offset=0, x_offset=0, offset_angle=0, width=450, height=450):

    inst = create_l_system(iterations, axiom, rules)

    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(width, height)

    if color:
        wn.bgcolor('black')

    t.up()    
    t.backward(-x_offset)
    t.left(90)
    t.backward(-y_offset)
    t.left(offset_angle)
    t.down()
    t.speed(0)
    t.pensize(size)
    draw_l_system(t, inst, angle, length, color)
    t.hideturtle()
    
    wn.exitonclick()


with open('fractals.json') as infile:
    fractals = json.load(infile)

"""
Fractal Options:

- "32-Segment-Curve"
- "Box-Fractal"
- "Dragon-Curve"
- "Twin-Dragon-Curve"
- "ThreeDragon-Curve"
- "TerDragon-Curve"
- "Levy-C-Curve"
- "Hilberts-Curve"
- "Hilbert-Curve-II"
- "Koch-Snowflake"
- "Peano-Curve"
- "Peano-Gosper-Curve"
- "Quadratic-Koch-Island"
- "Sierpinski-Arrowhead"
- "Sierpinski-Curve"
- "Siepinski-Sieve"
- "Quadratic-Snowflake"
- "Board"
- "Cross"
- "Cross-2"
- "Pentaplexity"
- "Tiles"
- "Rings"
- "Krishna-Anklets"
- "Triangle"
- "Quadratic-Gosper"
- "Crystal"
- "Moore-Curve"

"""
# 32-segment curve
title = "ThreeDragon-Curve"
fractal = fractals[title]

axiom = fractal['axiom']
rules = fractal['rules']
iterations = fractal['iterations']
angle = fractal['angle']

main(iterations, axiom, rules, angle)