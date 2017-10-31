gWIDTH = 300
PAGESIZE = 500
OFFCURVEPOINT = 6
ONCURVEPOINT = 15
FRAMES = 80
DELTA = 68


for frame in range(FRAMES+1):
    newPage(PAGESIZE, PAGESIZE)
    frameDuration(1/20)
    
    fill(0)
    rect(0,0, PAGESIZE, PAGESIZE)
    translate(PAGESIZE/2, PAGESIZE/2)
    
    factor = sin(pi * frame/FRAMES)
    
    for i in range(4):
        save()
        rotate(i*90)
        translate(-gWIDTH/2, -gWIDTH/2)
    
        fill(0,0,0,0)
        stroke(1)
        newPath()
        moveTo((149, 0))
        curveTo((232+(DELTA*factor), 0), (300, 68-(DELTA*factor)), (300, 150))
        drawPath()
        restore()
    
    for i in range(4):
        save()
        rotate(i*90)
        translate(-gWIDTH/2, -gWIDTH/2)
        fill(1, 0, 0, 1)
        stroke(0,0,0,0)
        oval(149-ONCURVEPOINT/2, 0-ONCURVEPOINT/2, ONCURVEPOINT, ONCURVEPOINT)
    
        fill(0,0,1,1)
        rect(232-OFFCURVEPOINT/2+(DELTA*factor), 0-OFFCURVEPOINT/2, OFFCURVEPOINT, OFFCURVEPOINT)
        rect(68-OFFCURVEPOINT/2-(DELTA*factor), 0-OFFCURVEPOINT/2, OFFCURVEPOINT, OFFCURVEPOINT)
        restore()

saveImage("test.gif")