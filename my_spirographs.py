import sys, random, argparse
import numpy as np
import math
import turtle
import random
from PIL import Image
from datetime import datetime    
from fractions import gcd

width, height = 100, 100
R = int(random.randint(50, min(width, height)//2))
r = int(random.randint(10, 9*R//10))
l = random.uniform(0.1, 0.9)
k = random.uniform(0.1, 0.9)
xc = random.randint(-width//2, width//2)
yc = random.randint(-height//2, height//2)
gcdVal = math.gcd(r, R)
col = (random.random(),
       random.random(),
       random.random())
t = turtle.Turtle()
foo = int(r/math.gcd(R,r)) * 360
power_K = 360 * (k**-1)
nRot = r//gcdVal
eee = int(R/math.gcd(r, R))
def draw():
    t.speed(0)
    # draw rest of points

    #for i in range(0,360 * (r//gcdVal) + 1, 5):   
    for i in range(0,foo, 5):
        #coordinates = ""
        a = math.radians(i)
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        print(i," / ",  str(360 * eee + 5))
        if i == 0:
            t.up()
        else:
            t.down()
        #if i == 3:
        #    coordinates = a
        #if a != coordinates:
        t.setpos(xc + x, yc + y)
    # done - hide turtle
    t.hideturtle()
    turtle.mainloop()

    i = 0
 #   while True:
 #       #t.color(random.uniform(0.1, 0.9),random.uniform(0.1, 0.9),random.uniform(0.1, 0.9))
 #       #if i % 2 == 0:
 #       #    t.color(1,0,0)
 #       #else:
 #       #    t.color(0,0,1)
 #       
 #       
 #       foo = int(r/math.gdc(R,r)) * 360
 #       a = math.radians(i)
 #       x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
 #       y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
 #       print(i," / ",a)
 #   
 #       if i != 0 and [xc + x, yc + y] == start_coordinates:
 #           break
 #       if i == 0:
 #           t.up()
 #       else:
 #           t.down()
 #       #if i == 3:
 #       #    coordinates = a
 #       #if a != coordinates:
 #       
 #       t.setpos(xc + x, yc + y)
 #       i += 5
    # done - hide turtle
    t.hideturtle()
    turtle.mainloop()

draw()