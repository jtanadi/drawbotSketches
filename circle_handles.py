from fontTools.pens.cocoaPen import CocoaPen
f = CurrentFont()
g1 = f["O"]
g2 = f["P"]
gWIDTH = g1.width
PAGESIZE = 500
OFFCURVEPOINT = 6
ONCURVEPOINT = 15
FRAMES = 20

def drawGlyph(glyph):
    pen = CocoaPen(f)
    glyph.draw(pen)
    drawPath(pen.path)

def getOffCurvePoints(glyph):
    return [(point.x, point.y) for contour in glyph for point in contour.points if point.type == "offCurve"]
    
def getOnCurvePoints(glyph):
    return [(point.x, point.y) for contour in glyph for point in contour.points if point.type != "offCurve"]
        
def getOffCurveDelta(points1, points2):
    return [(points2[i][0] - points1[i][0], points2[i][1] - points1[i][1])for i in range(len(points1))]

offCurveListG1 = getOffCurvePoints(g1)
offCurveListG2 = getOffCurvePoints(g2)
offCurveListDelta = getOffCurveDelta(offCurveListG1, offCurveListG2)

for frame in range(FRAMES+1):
    factor = frame / (FRAMES)
    newPage(PAGESIZE, PAGESIZE)
    fill(0)
    rect(0,0, PAGESIZE, PAGESIZE)
    translate(PAGESIZE/2-gWIDTH/2, PAGESIZE/2-gWIDTH/2)

    for i in range(len(offCurveListG1)):
        fill(0, 0, 1, 1)
        rect((offCurveListG1[i][0]-OFFCURVEPOINT/2)+(offCurveListDelta[i][0]*factor), (offCurveListG1[i][1]-OFFCURVEPOINT/2)+(offCurveListDelta[i][1]*factor), OFFCURVEPOINT, OFFCURVEPOINT)
    
    for x, y in getOnCurvePoints(g1):
        fill(1, 0, 0, 1)
        oval(x-ONCURVEPOINT/2, y-ONCURVEPOINT/2, ONCURVEPOINT, ONCURVEPOINT)
                
saveImage("test.gif")    
