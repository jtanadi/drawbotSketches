from _lib.Bezier import Bezier

C1 = (50, 0)
C2 = (250, 300)
C3 = (250, 300)
C4 = (450, 0)
PAGESIZE = 500
CIRCSIZE = 10
NPOINTS = 20
FRAMES = 40

b = Bezier(C1, C2, C3, C4)
yList = []

for frame in range(FRAMES+1):
    factor = sin(pi * frame /FRAMES)
    
    newPage(PAGESIZE, PAGESIZE)
    fill(0)
    rect(0,0, PAGESIZE, PAGESIZE)
    translate(0, 100)

    for n in range(NPOINTS+1):
        t = float(n) / NPOINTS
        x, y = b.findPoint(t)
        y = y-(factor * y)+100

        stroke(1)
        oval(x-CIRCSIZE/2, y-CIRCSIZE/2, CIRCSIZE, CIRCSIZE)

saveImage("_gifs/bezier_breathing.gif")