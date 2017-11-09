PAGESIZE = 600
SQUARE = 40
FRAMES = 3

def drawSlash(x, y):
    if random() > 0.5:
        line((x, y), (x + SQUARE, y + SQUARE))
    else:
        line((x, y + SQUARE), (x + SQUARE, y))


for frame in range(FRAMES):
    newPage(PAGESIZE, PAGESIZE)
    frameDuration(1/5)

    fill(0)
    rect(0, 0, PAGESIZE, PAGESIZE)

    fill(None)
    stroke(1)
    strokeWidth(10)
    lineCap("square")

    for y in range(0, PAGESIZE, SQUARE):
        for x in range(0, PAGESIZE, SQUARE):
            drawSlash(x, y)

saveImage("_gifs/tenPrint.gif")