"""
This module is to be used in addition to DrawBot primitive shapes. IT IS DEPENDENT ON DB MODULE.
It has shape objects that are drawn from a center point, not from the bottom left corner.

Currently there are 3 supported primitive shapes:
  - CRect: Rectangle if both width & height are provided. Square object if only 1 size provided.
  - COval: Oval if both width & height are provided. Circle object if only 1 size provided.
  - CTriangle: Non-eq. triangle if both width & height are provided.
    Eq. triangle if only 1 size provided. ### STILL TK ###
"""

from drawBot import *

class CPrimitives(object):
    """
    Parent primitive shape class.
    Not sure if this is useful to have yet, but here just in case.
    """
    def __init__(self):
        pass

    def __str__(self):
        print "Primitive shape"

class CRect(CPrimitives):
    """
    CRectangle object. Base arguments are: (width, height)
    If height isn't specified, height = width (ie. the object is a square).

    Use draw(px, py) method to draw the object:

    square1 = CRect(100)  -->  Instantiates the object as square1

    square1.draw(20, 60)  -->  Draws square1 with centerpoint 20, 60
    """
    def __init__(self, width, height=None):
        CPrimitives.__init__(self)
        if height is None:
            height = width

        self.width = width
        self.height = height

    def __str__(self):
        return "CRect object with width %s and height %s" %(self.width, self.height)

    def setSize(self, width, height=None):
        """
        Set new size of CRect object.
        Input arguments are: width, height

        If height isn't specified, width will be used (ie. object is square)
        """
        if height is None:
            height = width

        self.width = width
        self.height = height

    def getWidth(self):
        """
        Get width of CRect object.
        """
        return self.width

    def getHeight(self):
        """
        Get height of CRect object.
        """
        return self.height

    def isSquare(self):
        """
        Determines if CRect object is a square.
        Returns a boolean.
        """
        if self.height == self.width:
            return True
        return False

    def draw(self, x, y):
        """
        Draw CRect object from center point.
        Input arguments are: x, y (center points, not tuple).
        """
        rect(x - self.width / 2, y - self.height / 2, self.width, self.height)


class COval(CPrimitives):
    """
    COval object. Base arguments are: (width, height)
    If height isn't specified, height = width (ie. the object is a circle).

    Use draw(px, py) method to draw the object:

    circle1 = COval(100)  -->  Instantiates the object as circle1

    circle1.draw(20, 80)  -->  Draws circle1 with centerpoint (20, 80)
    """
    def __init__(self, width, height=None):
        CPrimitives.__init__(self)
        if height is None:
            height = width

        self.width = width
        self.height = height

    def __str__(self):
        return "COval object with width %s and height %s" %(self.width, self.height)

    def setSize(self, width, height=None):
        """
        Set new size of COval object.
        Input arguments are: width, height

        If height isn't specified, width will be used (ie. object is circle)
        """
        if height is None:
            height = width

        self.width = width
        self.height = height

    def getWidth(self):
        """
        Get width of COval object.
        """
        return self.width

    def getHeight(self):
        """
        Get height of COval object.
        """
        return self.height

    def isCircle(self):
        """
        Determines if COval object is a circle.
        Returns a boolean.
        """
        if self.height == self.width:
            return True
        return False

    def draw(self, x, y):
        """
        Draw CRect object from center point.
        Input arguments are: x, y (center points, not tuple).
        """
        oval(x - self.width / 2, y - self.height / 2, self.width, self.height)


# Old drawTriangle below. Need to figure out more precise method (using centroid).

    # def drawTriangle(self, px, py, size):
    #     save()
    #     translate(-size/2, -size/3)
    #     fill(0, 0, 1, 1)
    #     newPath()
    #     moveTo((px, py))
    #     lineTo((px+size/2, py+size))
    #     lineTo((px+size, py))
    #     lineTo((px, py))
    #     closePath()
    #     drawPath()
    #     restore()
