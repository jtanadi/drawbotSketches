PAGESIZE = 1000
FRAMES = 10

fontsList = [f for f in installedFonts() if f[0] != "."]


def drawLetter(i):
    font(fontsList[i])
    fontSize(1000)
    text("hey!", (0, 0))

for frame in range(FRAMES):
    r = frame / FRAMES

    newPage(PAGESIZE * 2, PAGESIZE)

    fill(1)
    rect(0, 0, PAGESIZE * 2, PAGESIZE)
    save()
    translate(100, 100)

    for i in range(int(len(fontsList))):
        save()

        path = BezierPath()

        path.moveTo((i * r, -100))
        path.lineTo((i * r + 900 / len(fontsList), 0))
        path.lineTo((i * r + 900 / len(fontsList), PAGESIZE))
        path.lineTo((i * r, PAGESIZE))
        path.closePath()
        clipPath(path)
        fill(random(), random(), random(), 1)
        drawLetter(i)
        restore()

    restore()
    
saveImage("_gifs/fontTest.gif")