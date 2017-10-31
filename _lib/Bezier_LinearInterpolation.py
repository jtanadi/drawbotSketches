"""
Bezier object
Inputs are 4 points (2-on curves & 2 off-curves) expressed as (x, y) tuples

Bezier().findPoints()
Requires Bezier object to be instantiated (eg. bezier1 = Bezier(p1, p2, p3, p4))
Input is k; output is a list of points expressed as (x, y) tuples. The last pair is the point on curve.

Points along t are calculated with the formula:
point = p1 + k*(p2-p1); k is fraction; p1 is first point, p2 is last point, so p2-p1 is length of line.
"""

class Bezier(object):
    def __init__(self, p1, p2, p3, p4):
        assert type(p1) is tuple and type(p2) is tuple and type(p3) is tuple and type(p4) is tuple
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
    
    def findPoints(self, k):
        ax = self.p1[0] + k * (self.p2[0] - self.p1[0])
        ay = self.p1[1] + k * (self.p2[1] - self.p1[1])

        bx = self.p2[0] + k * (self.p3[0] - self.p2[0])
        by = self.p2[1] + k * (self.p3[1] - self.p2[1])

        cx = self.p3[0] + k * (self.p4[0] - self.p3[0])
        cy = self.p3[1] + k * (self.p4[1] - self.p3[1])

        dx = ax + k * (bx - ax)
        dy = ay + k * (by - ay)
        
        ex = bx + k * (cx - bx)
        ey = by + k * (cy - by)

        fx = dx + k * (ex - dx)
        fy = dy + k * (ey - dy)

        return [(ax, ay), (bx, by), (cx, cy), (dx, dy), (ex, ey), (fx, fy)]