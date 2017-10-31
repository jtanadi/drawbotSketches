# Formula to find point at fraction of line / to divide line into eq. parts:
# point = p1 + k*(p2-p1); k is fraction; p1 is first point, p2 is last point, so p2-p1 is length of line.

C1 = (50, 325)
C2 = (300, 50)
C3 = (350, 400)
C4 = (450, 100)
PAGESIZE = 500
CIRCSIZE = 15
CIRCSIZESMALL = 7
RECTSIZE = 10
FRAMES = 40

def findPointOnCurve(p1, p2, p3, p4, k):
    ax = p1[0] + k*(p2[0]-p1[0])
    ay = p1[1] + k*(p2[1]-p1[1])

    bx = p2[0] + k*(p3[0]-p2[0])
    by = p2[1] + k*(p3[1]-p2[1])

    cx = p3[0] + k*(p4[0]-p3[0])
    cy = p3[1] + k*(p4[1]-p3[1])

    dx = ax + k*(bx-ax)
    dy = ay + k*(by-ay)
    
    ex = bx + k*(cx-bx)
    ey = by + k*(cy-by)

    fx = dx + k*(ex-dx)
    fy = dy + k*(ey-dy)

    return [(ax, ay), (bx, by), (cx, cy), (dx, dy), (ex, ey), (fx, fy)]

def drawCircle(px, py, size):
    oval(px-size/2, py-size/2, size, size)

def drawLine(p1, p2):
    newPath()
    moveTo(p1)
    lineTo(p2)
    drawPath()

def drawTriangle(p, size):
    x = p[0]
    y = p[1]

    save()
    
    translate(-size/2, -size/3)
    fill(0, 0, 1, 1)
    newPath()    
    moveTo((x, y))
    lineTo((x+size/2, y+size))
    lineTo((x+size, y))
    lineTo((x, y))
    closePath()
    drawPath()

    restore()

for frame in range(FRAMES):
    k = sin(pi * frame/FRAMES)

    pointsList = findPointOnCurve(C1, C2, C3, C4, k)
    ax, ay = pointsList[0]
    bx, by = pointsList[1]
    cx, cy = pointsList[2]
    dx, dy = pointsList[3]
    ex, ey = pointsList[4]
    fx, fy = pointsList[5]

    newPage(PAGESIZE, PAGESIZE)
    fill(0, 0, 0, 1)
    rect(0, 0, PAGESIZE, PAGESIZE)

    fill(0)
    stroke(1)
    newPath()
    moveTo(C1)
    curveTo(C2, C3, C4)
    drawPath()

    stroke(1, 1, 1, 0.5)
    drawLine(C1, C2)
    drawLine(C3, C4)
    lineDash(4)
    drawLine(C2, C3)

    stroke(0, 0, 0, 0)
    lineDash(0)
    drawTriangle(C2, RECTSIZE)
    drawTriangle(C3, RECTSIZE)

    fill(0,1,0,1)
    stroke(0,0,0,0)
    rect(C1[0]-RECTSIZE/2, C1[1]-RECTSIZE/2, RECTSIZE, RECTSIZE)
    rect(C4[0]-RECTSIZE/2, C4[1]-RECTSIZE/2, RECTSIZE, RECTSIZE)
    
    fill(0, 0, 1, 1)
    stroke(0, 0, 0, 0)
    drawCircle(ax, ay, CIRCSIZESMALL)
    drawCircle(bx, by, CIRCSIZESMALL)
    drawCircle(cx, cy, CIRCSIZESMALL)

    stroke(0, 0, 1, 0.5)
    drawLine((ax, ay), (bx, by))
    drawLine((bx, by), (cx, cy))
    
    fill(0, 1, 0, 1)
    stroke(0, 0, 0, 0)
    drawCircle(dx, dy, CIRCSIZESMALL)
    drawCircle(ex, ey, CIRCSIZESMALL)

    stroke(0, 1, 0, 0.5)
    drawLine((dx, dy), (ex, ey))

    fill(1, 0, 0, 1)
    stroke(0,0,0,0)
    drawCircle(fx, fy, CIRCSIZE)

saveImage("bezier_animation2.gif")