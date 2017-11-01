from _lib.Shapes import Shapes

s = Shapes()

PAGESIZE = 600
CIRCSIZE = 300
TOTALNUM = 100
FRAMES = 40



for frame in range(1, FRAMES+1):
    f = sin(2 * pi * frame / FRAMES)
    t = cos(2 * pi * frame / FRAMES)
    newPage(PAGESIZE, PAGESIZE)
    fill(0)
    rect(0,0, PAGESIZE, PAGESIZE)

    translate(PAGESIZE / 2, PAGESIZE / 2)

    save()
    translate(TOTALNUM * t, 0)
    for i in range(0, TOTALNUM):
        n = i / TOTALNUM
        print n
        fill(n, n, n, 1)
        
        if i >= 35:
            save()
            rotate(45*i)
            s.drawSquare(0, 0, CIRCSIZE * (1 - n))
            restore()

        s.drawCircle(0, 0, CIRCSIZE * (1 - n))
        translate(0, TOTALNUM/50*f)
    restore()

saveImage("_gifs/circle_fade_test.gif")