PAGESIZE = 600
SQUARE = 20
FRAMES = 20

def drawSlash(x, y):
    if random() > 0.5:
        fill(random(), random(), 1, 1)
        rect(x, y, SQUARE, SQUARE)

    else:
        fill(1, random(), random(), 1)
        oval(x, y, SQUARE, SQUARE)


for frame in range(FRAMES):
    newPage(PAGESIZE, PAGESIZE)
    frameDuration(1/5)

    fill(0)
    rect(0, 0, PAGESIZE, PAGESIZE)

    for y in range(0, PAGESIZE, SQUARE):
        for x in range(0, PAGESIZE, SQUARE):
            drawSlash(x, y)

saveImage("_gifs/tenPrint_colors_circles.gif")