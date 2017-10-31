PAGESIZE = 600
TOTALCOLS = TOTALROWS = 8
FRAMES = 60

def drawLine(angle, scl):
    fill(None)
    stroke(1)
    strokeWidth(1/scl)
    save()
    scale(scl)
    translate(PAGESIZE/5, PAGESIZE/5)
    rotate(angle*5)
    translate(-PAGESIZE/5, -PAGESIZE/5)
    line((0, 0), (PAGESIZE/2.5, PAGESIZE/2.5))
    restore()

for frame in range(FRAMES):
    f = sin(2 * pi * frame / FRAMES)
    newPage(PAGESIZE, PAGESIZE)
    fill(0)
    rect(0, 0, PAGESIZE, PAGESIZE)
    translate(-PAGESIZE / TOTALROWS / 1.5, 0)

    for col in range(TOTALCOLS*2):
        save()
        translate(0, col*PAGESIZE/TOTALCOLS/2)
        for row in range(TOTALROWS*3):
            drawLine(f * row, 1 / TOTALROWS)
            translate(PAGESIZE / TOTALROWS / 2, 0)
        restore()

saveImage("_gifs/grid_rotate.gif")