P = [(20, 50), (150, 400), (300, 350), (480, 50)]
CIRCSIZE = 10
CANVAS = 500

newPage(CANVAS, CANVAS)

fill(None)
stroke(0)

newPath()
moveTo(P[0])
curveTo(P[1], P[2], P[3])
drawPath()

stroke(0, 0, 1, 1)
for i in range(len(P)-1):
    newPath()
    moveTo(P[i])
    lineTo(P[i+1])
    drawPath()

fill(1, 0, 0, 1)
stroke(None)
for i in range(len(P)):
    oval(P[i][0]-CIRCSIZE/2, P[i][1]-CIRCSIZE/2, CIRCSIZE, CIRCSIZE)

def calcSlope(Pa, Pb):
    return (Pb[1] - Pa[1]) / (Pb[0] - Pa[0])

def calcPerpSlope(Pa, Pb):
    return 1 / calcSlope(Pa, Pb) * -1

def calcPointFromDist1((x1, y1), m, d):
    
    c = 1 / (1 + m ** 2) ** .5
    s = m / (1 + m ** 2) ** .5
    
    x = x1 - d * c
    y = y1 - d * s

    return (x, y)

def calcPointFromDist2((x1, y1), m, d):
    
    c = 1 / (1 + m ** 2) ** .5
    s = m / (1 + m ** 2) ** .5
    
    x = x1 + d * c
    y = y1 + d * s

    return (x, y)

fill(None)
stroke(0, 1, 0, 1)

for i in range(len(P)-1):
    mPerp = calcPerpSlope(P[i], P[i+1])
    newPath()
    if i != 0:
        moveTo(calcPointFromDist1(P[i], mPerp, 20))
        lineTo(calcPointFromDist1(P[i+1], mPerp, 20))
    else:
        moveTo(calcPointFromDist2(P[i], mPerp, 20))
        lineTo(calcPointFromDist2(P[i+1], mPerp, 20))
    drawPath()



# mPerp = calcPerpSlope(P[0], P[1])
x1, y1 = calcPointFromDist2(P[0], calcPerpSlope(P[0], P[1]), 20)
x2, y2 = calcPointFromDist1(P[1], calcPerpSlope(P[1], P[2]), 20)
x3, y3 = calcPointFromDist1(P[2], calcPerpSlope(P[2], P[3]), 20)

m1 = calcSlope(P[0], P[1])
m2 = calcSlope(P[1], P[2])
m3 = calcSlope(P[2], P[3])

b1 = y1 - (m1 * x1)
b2 = y2 - (m2 * x2)
b3 = y3 - (m3 * x3)

xA = (b1 - b2) / (m2 - m1)
yA = (m1 * xA) + b1

xB = (b2 - b3) / (m3 - m2)
yB = (m2 * xB) + b2

stroke(None)
fill(1, 0, 1, 1)
oval(xA - CIRCSIZE/2, yA - CIRCSIZE/2, CIRCSIZE, CIRCSIZE)
oval(xB - CIRCSIZE/2, yB - CIRCSIZE/2, CIRCSIZE, CIRCSIZE)

newPath()
moveTo(calcPointFromDist2(P[0], calcPerpSlope(P[0], P[1]), 20))
curveTo((xA, yA), (xB, yB), calcPointFromDist1(P[3], mPerp, 20))
drawPath()

"""

m1 = calcSlope(P[0], P[1])
m2 = calcSlope(P[1], P[2])

x1, y1 = calcPerpPoint2(P[0], 20)

b1 = y1 - (m1 * x1)
b2 = y2 - (m2 * x2)

m2 * x3 + b2 = m1 * x3 + b1

(m2 * x3) - (m1 * x3) = b1 - b2

x3 = (b1 - b2) / (m2 - m1)






line1X, line1Y = calcPerpPoint2(P[0], 20)
line2X, line2Y = calcPerpPoint2(P[0], 20)

y - line1Y = m1 * (x - line1X)
y = m1 * (x - line1X) + line1Y
y = (m1 * x) - (m1 * line1X) + line1Y

(m1 * x) - (m1 * line1X) + line1Y = (m2 * x) - (m2 * line2X) + line2Y
(m1 * x) - (m2 * x) = (m1 * line1X) - (m2 * line2X) + line2Y - line1Y


"""