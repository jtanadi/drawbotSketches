class Bezier(object):
    def __init__(self, p1, p2, p3, p4):
        assert type(p1) is tuple and type(p2) is tuple and type(p3) is tuple and type(p4) is tuple
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def findPoint(self, t):
        x = self.p1[0] * self.B1(t) + self.p2[0] * self.B2(t) + self.p3[0] * self.B3(t) + self.p4[0] * self.B4(t)
        y = self.p1[1] * self.B1(t) + self.p2[1] * self.B2(t) + self.p3[1] * self.B3(t) + self.p4[1] * self.B4(t)

        return (x, y)

    def B1(self, t):
        return t**3
        
    def B2(self, t):
        return 3 * t **2*(1-t)

    def B3(self, t):
        return 3*t*(1-t)**2
        
    def B4(self, t):
        return (1-t)**3