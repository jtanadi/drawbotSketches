from fontTools.pens.cocoaPen import CocoaPen

font = CurrentFont()
glyph = font["g"] 
circSize = 30
squareSize = 12
# pointsList = [(glyph[c][s][p].x, glyph[c][s][p].y) for c in range(len(glyph)) for s in range(len(glyph[c])) for p in range(len(glyph[c][s]))]

pointsList = [(p.x, p.y, p.type) for c in glyph for p in c.points]

newPage("Folio")

translate(30, 300)

for i in range(len(pointsList)):
    if pointsList[i][2] != "offCurve":
        blendMode("multiply")
        fill(1, 0, 0, 1)
        save()
        translate(-circSize/2, -circSize/2)
        oval(pointsList[i][0], pointsList[i][1], circSize, circSize)
        restore()
    else:
        fill(0, 0, 1, 1)
        save()
        translate(-squareSize/2, -squareSize/2)
        rect(pointsList[i][0], pointsList[i][1], squareSize, squareSize)
        restore()
        
fill(0, 0, 0, .25)
#stroke(0, 0, 0, 1)        
pen = CocoaPen(font)
glyph.draw(pen)
drawPath(pen.path)