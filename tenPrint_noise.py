PAGESIZE = 500
SQUARE = 10
FRAMES = 40

def drawSlash(x, y):
    if random() > 0.5:
        rect(x, y, SQUARE+0.5, SQUARE+0.5)


for frame in range(FRAMES):
    newPage(PAGESIZE, PAGESIZE)
    fill(0)
    rect(0, 0, PAGESIZE, PAGESIZE)

    fill(1)

    for y in range(0, PAGESIZE, SQUARE):
        for x in range(0, PAGESIZE, SQUARE):
            drawSlash(x, y)

saveImage("_gifs/tenPrint_noise.gif")