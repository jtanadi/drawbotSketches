PAGESIZE = 600
SQUARE = 20
FRAMES = 20

def drawSlash(x, y):
    if random() > 0.5:
        for i in range(3):
            if i == 0:
                fill(255/255, 224/255, 65/255, 1)

            elif i == 1:
                fill(36/255, 101/255, 168/255, 1)

            else:
                fill(238/255, 110/255, 147/255, 1)

            rect(x, y + SQUARE * i / 3, SQUARE, SQUARE / 3)

    else:
        for i in range(3):
            if i == 0:
                fill(249/255, 115/255, 45/255, 1)

            elif i == 1:
                fill(79/255, 197/255, 150/255, 1)

            else:
                fill(58/255, 102/255, 179/255, 1)

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