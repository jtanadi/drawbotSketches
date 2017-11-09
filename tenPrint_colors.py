PAGESIZE = 600
SQUARE = 20
FRAMES = 20

def drawSlash(x, y):
    if random() > 0.5:
        for i in range(3):
            if i == 0:
                fill(251/255, 217/255, 58/255, 1)

            elif i == 1:
                fill(48/255, 95/255, 149/255, 1)

            else:
                fill(235/255, 123/255, 148/255, 1)

            rect(x, y + SQUARE * i / 3, SQUARE, SQUARE / 3)

    else:
        for i in range(3):
            if i == 0:
                fill(86/255, 188/255, 148/255, 1)

            elif i == 1:
                fill(233/255, 117/255, 60/255, 1)

            else:
                fill(72/255, 115/255, 181/255, 1)

            rect(x + SQUARE * i / 3, y, SQUARE / 3, SQUARE)


for frame in range(FRAMES):
    newPage(PAGESIZE, PAGESIZE)
    frameDuration(1/5)

    fill(0)
    rect(0, 0, PAGESIZE, PAGESIZE)

    for y in range(0, PAGESIZE, SQUARE):
        for x in range(0, PAGESIZE, SQUARE):
            drawSlash(x, y)

saveImage("_gifs/tenPrint_colors2.gif")