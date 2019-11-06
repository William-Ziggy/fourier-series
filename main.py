from graphics import *
import math, cmath


#The function we want to approximate:
def f(t):
    return math.cos(2*math.pi*t)+1j*math.sin(2*math.pi*t)

def integrand(x, n):
    return f(x)*math.e**(-n*2*math.pi*1j*x)

def c(n):
    num_iterations = 100

    delta_x = 1/num_iterations

    sum = 0
    for i in range(0, num_iterations+1):
        x = i*delta_x
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

antal = 200

points = []

scale = 100
import numpy as np

intervall = np.linspace(0, 1, num=antal)
#Plotting the actual function
for t in intervall:
    ptf = Point(ctr+scale*f(t).real, ctr-scale*f(t).imag)
    ptf.setFill("white")
    ptf.draw(win)


N = 20

origin = Point(ctr, ctr)

vecList = []
tipList = []

nVec = np.linspace(-N/2, N/2, num=N)
print(nVec)

points = []


cList = []

for t in intervall:

    lastPt = origin

    re = 0
    im = 0
    for n in nVec:
        z=scale*c(n)*math.e**(n*2*math.pi*1j*t)
        print(c(n))
        re = re + z.real
        im = im + z.imag
        newPt = Point(ctr+re, ctr-im)

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
    if not t==0:
        line = Line(points[-2], points[-1])
        line.setFill('yellow')
        line.draw(win)


    update(60)

    for v, tipv in zip(vecList, tipList):
        v.undraw()
        tipv.undraw()


win.getMouse()
