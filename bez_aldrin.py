from vanilla import *
from drawBot import *
from drawBot.ui.drawView import DrawView
from _lib.Shapes import Shapes

C1 = (25, 250)
C4 = (475, 250)

PAGESIZE = 500
CIRCSIZE = 12
CIRCSIZESMALL = 6
RECTSIZE = 10
FRAMES = 40

class BezierPreview(object):
    def __init__(self):
        self.p2x = 200
        self.p2y = 350
        self.p3x = 300
        self.p3y = 150
        self.k = 0.5
        self.draw1st = 0
        self.draw2nd = 0

        self.buildUI()

    def buildUI(self):
        minX = C1[0]
        maxX = C4[0]

        minY = 25
        maxY = PAGESIZE - 25

        row = 10

        self.w = Window((1000, 800), "Bez Aldrin")

        self.w.p2xText = TextBox((10, row, 100, 17),
                                 "Off-Curve 1 x:")

        self.w.p2xSlider = Slider((10, row + 17, 200, 20),
                                  minValue=minX,
                                  maxValue=maxX,
                                  value=self.p2x,
                                  callback=self.p2xSliderCallback)

        row += 45
        self.w.p2yText = TextBox((10, row, 100, 17),
                                 "Off-Curve 1 y:")

        self.w.p2ySlider = Slider((10, row + 17, 200, 20),
                                  minValue=minY,
                                  maxValue=maxY,
                                  value=self.p2y,
                                  callback=self.p2ySliderCallback)

        row += 90
        self.w.p3xText = TextBox((10, row, 100, 17),
                                 "Off-Curve 2 x:")
        self.w.p3xSlider = Slider((10, row + 17, 200, 20),
                                  minValue=minX,
                                  maxValue=maxX,
                                  value=self.p3x,
                                  callback=self.p3xSliderCallback)

        row += 45
        self.w.p3yText = TextBox((10, row, 100, 17),
                                 "Off-Curve 2 y:")
        self.w.p3ySlider = Slider((10, row + 17, 200, 20),
                                  minValue=minY,
                                  maxValue=maxY,
                                  value=self.p3y,
                                  callback=self.p3ySliderCallback)

        row += 90
        self.w.kText = TextBox((10, row, 100, 17),
                               "Point Position")
        self.w.kSlider = Slider((10, row + 17, 200, 20),
                                minValue=0,
                                maxValue=1,
                                value=self.k,
                                callback=self.kSliderCallback)

        row += 90
        self.w.draw1stCheck = CheckBox((10, row, 200, 22),
                                       "Draw 1st Interpolation",
                                       callback=self.draw1stCheckCallback)

        row += 25
        self.w.draw2ndCheck = CheckBox((10, row, 200, 22),
                                       "Draw 2nd Interpolation",
                                       callback=self.draw2ndCheckCallback)

        row += 140
        self.w.generateButton = SquareButton((10, row, 200, 80),
                                             "Animate",
                                             callback=self.animateDrawing)

        self.w.canvas = DrawView((220, 10, -10, -10))

        self.drawCanvas()
        self.w.open()

    def p2xSliderCallback(self, sender):
        self.p2x = sender.get()
        self.drawCanvas()

    def p2ySliderCallback(self, sender):
        self.p2y = sender.get()
        self.drawCanvas()

    def p3xSliderCallback(self, sender):
        self.p3x = sender.get()
        self.drawCanvas()

    def p3ySliderCallback(self, sender):
        self.p3y = sender.get()
        self.drawCanvas()

    def kSliderCallback(self, sender):
        self.k = sender.get()
        self.drawCanvas()

    def draw1stCheckCallback(self, sender):
        self.draw1st = sender.get()
        self.drawCanvas()

    def draw2ndCheckCallback(self, sender):
        self.draw2nd = sender.get()
        self.drawCanvas()

    def drawCanvas(self):
        newDrawing()
        newPage(PAGESIZE, PAGESIZE)
        fill(1)
        rect(0, 0, PAGESIZE, PAGESIZE)

        self.pointsList = self.findPoints(C1, (self.p2x, self.p2y),
                                          (self.p3x, self.p3y), C4, self.k)

        self.drawOffCurvePoints()
        self.drawCurve()

        if self.draw1st == 1:
            self.draw1stInterpolation((self.pointsList[0][0], self.pointsList[0][1]),
                                      (self.pointsList[1][0], self.pointsList[1][1]),
                                      (self.pointsList[2][0], self.pointsList[2][1]))

        if self.draw2nd == 1:
            self.draw2ndInterpolation((self.pointsList[3][0], self.pointsList[3][1]),
                                      (self.pointsList[4][0], self.pointsList[4][1]))

        self.drawPointAtK((self.pointsList[5][0], self.pointsList[5][1]))
        self.w.canvas.setPDFDocument(pdfImage())

    def drawCurve(self):
        fill(None)
        stroke(0)
        lineDash(None)
        newPath()
        moveTo(C1)
        curveTo((self.p2x, self.p2y), (self.p3x, self.p3y), C4)
        drawPath()

        fill(0, 1, 0, 1)
        stroke(None)
        rect(C1[0]-RECTSIZE/2, C1[1]-RECTSIZE/2, RECTSIZE, RECTSIZE)
        rect(C4[0]-RECTSIZE/2, C4[1]-RECTSIZE/2, RECTSIZE, RECTSIZE)

    def drawOffCurvePoints(self):
        stroke(0, 0, 0, 0.5)
        line(C1, (self.p2x, self.p2y))
        line((self.p3x, self.p3y), C4)
        lineDash(4)
        line((self.p2x, self.p2y), (self.p3x, self.p3y))

        stroke(None)
        shapes.drawTriangle(self.p2x, self.p2y, RECTSIZE)
        shapes.drawTriangle(self.p3x, self.p3y, RECTSIZE)

    def draw1stInterpolation(self, (ax, ay), (bx, by), (cx, cy)):
        fill(None)
        stroke(0, 0, 1, 0.5)
        lineDash(None)
        line((ax, ay), (bx, by))
        line((bx, by), (cx, cy))

        fill(0, 0, 1, 1)
        stroke(None)
        shapes.drawCircle(ax, ay, CIRCSIZESMALL)
        shapes.drawCircle(bx, by, CIRCSIZESMALL)
        shapes.drawCircle(cx, cy, CIRCSIZESMALL)

    def draw2ndInterpolation(self, (dx, dy), (ex, ey)):
        fill(None)
        stroke(0, 1, 0, 0.5)
        line((dx, dy), (ex, ey))

        fill(0, 1, 0, 1)
        stroke(None)
        shapes.drawCircle(dx, dy, CIRCSIZESMALL)
        shapes.drawCircle(ex, ey, CIRCSIZESMALL)

    def drawPointAtK(self, (fx, fy)):
        fill(1, 0, 0, 1)
        stroke(None)

        shapes.drawCircle(fx, fy, CIRCSIZE)

    def findPoints(self, p1, p2, p3, p4, k):
        ax = p1[0] + k * (p2[0] - p1[0])
        ay = p1[1] + k * (p2[1] - p1[1])

        bx = p2[0] + k * (p3[0] - p2[0])
        by = p2[1] + k * (p3[1] - p2[1])

        cx = p3[0] + k * (p4[0] - p3[0])
        cy = p3[1] + k * (p4[1] - p3[1])

        dx = ax + k * (bx - ax)
        dy = ay + k * (by - ay)

        ex = bx + k * (cx - bx)
        ey = by + k * (cy - by)

        fx = dx + k * (ex - dx)
        fy = dy + k * (ey - dy)

        return [(ax, ay), (bx, by), (cx, cy), (dx, dy), (ex, ey), (fx, fy)]

    def animateDrawing(self, sender):
        newDrawing()

        for frame in range(FRAMES):
            k = sin(pi * frame / FRAMES)
            newPage(PAGESIZE, PAGESIZE)
            fill(1)
            rect(0, 0, PAGESIZE, PAGESIZE)

            animatePointsList = self.findPoints(C1, (self.p2x, self.p2y),
                                                (self.p3x, self.p3y), C4, k)

            self.drawOffCurvePoints()
            self.drawCurve()

            if self.draw1st == 1:
                self.draw1stInterpolation((animatePointsList[0][0], animatePointsList[0][1]),
                                          (animatePointsList[1][0], animatePointsList[1][1]),
                                          (animatePointsList[2][0], animatePointsList[2][1]))

            if self.draw2nd == 1:
                self.draw2ndInterpolation((animatePointsList[3][0], animatePointsList[3][1]),
                                          (animatePointsList[4][0], animatePointsList[4][1]))

            self.drawPointAtK((animatePointsList[5][0], animatePointsList[5][1]))

        saveImage("~/Desktop/bez_aldrin.gif")
        
shapes = Shapes()

BezierPreview()
