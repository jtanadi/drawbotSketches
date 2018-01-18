# Add import to use drawBot as module outside of the app
from drawBot import *

C1 = (50, 100)
C2 = (150, 400)
C3 = (350, 400)
C4 = (450, 100)
PAGESIZE = 500
CIRCSIZE = 15
RECTSIZE = 10
FRAMES = 40

#Cubic equation functions
def B1(t):
    return t**3
    
def B2(t):
    return 3*t**2*(1-t)

def B3(t):
    return 3*t*(1-t)**2
    
def B4(t):
    return (1-t)**3
    
def drawTriangle(C, size):
    x = C[0]
    y = C[1]
    
    save()
    translate(-size/2, -size/3)
    
    fill(0, 0, 1, 1)
    newPath()    
    moveTo((x, y))
    lineTo((x+size/2, y+size))
    lineTo((x+size, y))
    lineTo((x, y))
    drawPath()

    restore()

for frame in range(FRAMES):
    t = sin(pi * frame/FRAMES)
    # print t

    newPage(PAGESIZE, PAGESIZE)
    fill(0, 0, 0, 1)
    rect(0, 0, PAGESIZE, PAGESIZE)
    
    fill(0)
    stroke(1)
    newPath()
    moveTo(C1)
    curveTo(C2, C3, C4)
    drawPath()
    
    stroke(.25)
    newPath()
    moveTo(C1)
    lineTo(C2)
    moveTo(C4)
    lineTo(C3)
    drawPath()
    
    fill(0,1,0,1)
    stroke(0,0,0,0)
    rect(C1[0]-RECTSIZE/2, C1[1]-RECTSIZE/2, RECTSIZE, RECTSIZE)
    rect(C4[0]-RECTSIZE/2, C4[1]-RECTSIZE/2, RECTSIZE, RECTSIZE)
    
    x = C1[0] * B1(t) + C2[0] * B2(t) + C3[0] * B3(t) + C4[0] * B4(t)
    y = C1[1] * B1(t) + C2[1] * B2(t) + C3[1] * B3(t) + C4[1] * B4(t)
    
    fill(1, 0, 0, 1)
    oval(x-CIRCSIZE/2, y-CIRCSIZE/2, CIRCSIZE, CIRCSIZE)

    drawTriangle(C2, RECTSIZE)
    drawTriangle(C3, RECTSIZE)
  
saveImage("_gifs/bezier_animation1.gif")