from drawBot import *

"""
Set of functions to draw shapes from center point

drawTriangle(px, py, size)
drawCircle(px, py, size)
drawSquare(px, py, size)

"""
def cTriangle(px, py, width, height=None):
    if height is None:
        height = width

    save()
    translate(-width/2, -height/3)
    fill(0, 0, 1, 1)
    newPath()
    moveTo((px, py))
    lineTo((px+width/2, py+height))
    lineTo((px+width, py))
    lineTo((px, py))
    closePath()
    drawPath()
    restore()

def cOval(px, py, width, height=None):
    if height is None:
        height = width

    oval(px-width/2, py-height/2, width, height)

def cRect(px, py, width, height=None):
    if height is None:
        height = width

    rect(px-width/2, py-height/2, width, height)