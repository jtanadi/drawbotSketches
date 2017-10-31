from fontTools.pens.cocoaPen import CocoaPen

font = CurrentFont()
glyph = font["g"]
glyph2 = font["h"]

circSize = 30
squareSize = 12
totalFrame = 15

pList1 = [(p.x, p.y) for c in glyph for p in c.points if p.type != "offCurve"]
pList2 = [(p.x, p.y) for c in glyph2 for p in c.points if p.type != "offCurve"]
pDelta = [(pList2[i][0] - pList1[i][0], pList2[i][1] - pList1[i][1]) for i in range(len(pList1))]

for frame in range(totalFrame):
    factor = frame / totalFrame

    newPage(500,500)
    fill(0)
    rect(0,0, 500, 500)

    translate(112, 175)
    scale(.5)

    blendMode("normal")    
    fill(0)
    stroke(1,0,0,1)
    pen = CocoaPen(font)
    glyph.draw(pen)
    drawPath(pen.path)
    
    glyph2.draw(pen)
    drawPath(pen.path)
        
    for i in range(len(pList1)):
        blendMode("screen")
        fill(0, 0, 1, 1)
        stroke(0,0,0,0)
        save()
        translate(-circSize/2, -circSize/2)
        oval(pList1[i][0]+(pDelta[i][0]*factor), pList1[i][1]+(pDelta[i][1]*factor), circSize, circSize)
        restore()
    

        
saveImage("plotPointsofGlyph2.gif")
