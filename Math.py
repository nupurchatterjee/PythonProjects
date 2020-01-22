class Line:

    def __init__(self, coor1, coor2):

        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
         return  (self.coor1 - self.coor2)

    def slope(self):
        return self.coor2 * self.coor1
    

c1 = (1, 2)
c2 = (3, 4)

lineClass = Line(c1, c2)
lineClass.distance()
