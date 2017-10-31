from drawBot import *

class Shapes(object):
    """
    Class that contains methods to draw shapes with specified point as the center point.
    The class has no input, but each method takes in point x, point y, and size.

    Methods:
    drawTriangle(p, size)
    drawCircle(px, py, size)
    drawSquare(px, py, size)

    """
    def __init__(self):
        pass

    def drawTriangle(self, px, py, size):
        save()
        translate(-size/2, -size/3)
        fill(0, 0, 1, 1)
        newPath()
        moveTo((px, py))
        lineTo((px+size/2, py+size))
        lineTo((px+size, py))
        lineTo((px, py))
        closePath()
        drawPath()
        restore()

    def drawCircle(self, px, py, size):
        oval(px-size/2, py-size/2, size, size)
    
    def drawSquare(self, px, py, size):
        rect(px-size/2, py-size/2, size, size)