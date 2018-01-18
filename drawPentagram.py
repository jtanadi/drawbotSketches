PAGESIZE = 500
CIRCSIZE = 450
ANGLE = 144

def drawRadius():
    newPath()
    moveTo((0, 0))
    lineTo((CIRCSIZE/2, 0))
    drawPath()
    
def drawSide():
    save()
    drawRadius()
    rotate(ANGLE)
    drawRadius()
    
    translate(CIRCSIZE/2, 0)
    rotate(-144-18)
    newPath()
    moveTo((0, 0))
    lineTo((3.74*(CIRCSIZE) * sin(ANGLE/2), 0))
    drawPath()
    restore()
    
newPage(PAGESIZE, PAGESIZE)

translate(PAGESIZE/2, PAGESIZE/2)

fill(None)
stroke(0)
oval(0 - CIRCSIZE / 2, 0 - CIRCSIZE / 2, CIRCSIZE, CIRCSIZE) 

rotate(18)

for i in range(5):
    drawSide()
    rotate(72)