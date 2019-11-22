from graphics import *
import math, cmath


#The function we want to approximate:
def f(t):
    return t**3+1j*t-1-1j

def integrand(x, n):
    return f(x)*math.e**(-n*2*math.pi*1j*x)

def c(n):
    num_iterations = 1000

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


win = GraphWin("Fourier Series", size, size) #Window Initialization
win.setBackground("black")
win.autoflush = False

antal = 100

points = []

scale = 600
import numpy as np

intervall = np.linspace(0, 1, num=antal)
#Plotting the actual function
for t in intervall:
    ptf = Point(ctr+scale*f(t).real, ctr-scale*f(t).imag)
    ptf.setFill("blue")
    ptf.draw(win)


N = 20

origin = Point(ctr, ctr)

vecList = []
cirList = []
lines = []

nVec = np.linspace(-N/2, N/2, N+1)
points = []


cList = []

for n in nVec:
    cList.append(c(n))

testN = -N/2
print(scale*cList[(n+N/2).astype(int)]*math.e**(testN*2*math.pi*1j*t))

while True:
    for t in intervall:

        lastPt = origin

        re = 0
        im = 0
        for n in nVec:
            z=scale*cList[(n+N/2).astype(int)]*math.e**(n*2*math.pi*1j*t)
            re = re + z.real
            im = im + z.imag

            newPt = Point(ctr+re, ctr-im)

            dx = newPt.getX()-lastPt.getX()
            dy = newPt.getY()-lastPt.getY()
            mag = math.sqrt(dx**2+dy**2)

            vec = Line(lastPt, newPt)
            vec.setWidth(2)
            vec.setFill('white')
            vec.setArrow("last")

            cir = Circle(lastPt, mag)
            cir.setOutline('gray')

            vec.draw(win)
            cir.draw(win)

            vecList.append(vec)

            cirList.append(cir)

            lastPt = newPt

        points.append(newPt)
        if not t==0:
            line = Line(points[-2], points[-1])
            line.setFill('yellow')
            line.draw(win)
            lines.append(line)



        update(10)

        for v, cirv in zip(vecList, cirList):
            v.undraw()
            cirv.undraw()
    for l in lines:
        l.undraw()

win.getMouse()
