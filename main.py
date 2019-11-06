from graphics import *
import math, cmath


#The function we want to approximate:
def f(x):
    return x+math.pi

p = math.pi #Half of interval we want to plot


def simpsons(n, integrand):
    num_iterations = 1000

    delta_x = 2*p/num_iterations

    sum = 0
    for i in range(0, num_iterations+1):
        x = p+i*delta_x
        if i==0 or i==num_iterations:
            sum+=integrand(x, n)
        elif i%2==0:
            sum+=2*integrand(x, n)
        else:
            sum+=4*integrand(x, n)

    integral = delta_x/3 * sum
    return integral

size = 1000 #Size of window
ctr = size/2-1 #Centre of window


win = GraphWin("Mitt fönster", size, size) #Window Initialization
win.setBackground("black")
win.autoflush = False

antal = 100

speed = 2
points = []


import numpy as np

xList = np.linspace(-p, p, num=antal) #Defining a list of x values


scale = 10 #Scale of plot

#Plotting the actual function
for x in xList:
    ptf = Point(ctr+scale*x, ctr-scale*f(x))
    ptf.setFill("white")

    ptf.draw(win)

N = 30

#Calculate constants:
def aIntegrand(x, n):
    return f(x)*math.cos(n*math.pi*x/p)
def bIntegrand(x, n):
    return f(x)*math.sin(n*math.pi*x/p)

a0 = scale*(1/p * simpsons(0, aIntegrand))

an = []
bn = []

for n in range(1, N+1):
    an.append(1/p * simpsons(n, aIntegrand))
    bn.append(1/p * simpsons(n, bIntegrand))


origin = Point(ctr, ctr)

for x in xList:

    lastPt = origin
    vecList = []
    tipList = []

    y=0

    for n in range(1, N+1):
        y = y + scale*(an[n-1]*math.cos(n*math.pi*x/p) + bn[n-1]*math.sin(n*math.pi*x/p))
        print(ctr-y)
        newPt = Point(ctr+scale*x, ctr+-y+a0/2)

        vec = Line(lastPt, newPt)
        vec.setWidth(2)
        vec.setFill('white')

        tip = Circle(newPt, 2)
        tip.setFill('red')

        vec.draw(win)
        tip.draw(win)

        vecList.append(vec)
        tipList.append(tip)

        lastPt = newPt

    points.append(newPt)

    if not x==-p:
        line = Line(points[-2], points[-1])
        line.setFill('yellow')
        line.draw(win)


    update(60)

    for v, tipv in zip(vecList, tipList):
        v.undraw()
        tipv.undraw()

win.getMouse()

"""
while x<p:
    x+=h

    scale = 100

    origin = Point(ctr, ctr)
    y = 0

    lastPt = origin

    vecList = []
    tipList = []


    for k in range(0, N+1):
        i = k-N/2
        z = c(i)*(math.e**(-i*x*math.pi*1j/p))
        print(z)
        y = y + z.imag

        newPt = Point(ctr+x, ctr-y)

        vec = Line(lastPt, newPt)
        vec.setWidth(2)
        vec.setFill('white')

        tip = Circle(newPt, 2)
        tip.setFill('red')

        vec.draw(win)
        tip.draw(win)

        vecList.append(vec)
        tipList.append(tip)

        lastPt = newPt

    points.append(newPt)
    if not n==0:
        line = Line(points[-2], points[-1])
        line.setFill('yellow')
        line.draw(win)


    update(20)

    for v, tipv in zip(vecList, tipList):
        v.undraw()
        tipv.undraw()
    n+=1

win.getMouse()
"""
