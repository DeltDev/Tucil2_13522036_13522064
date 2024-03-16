#Objek titik

class Point:
    def __init__(self,x,y,pointName):
        self.x = x
        self.y = y
        self.pointName = pointName
    def printPoint(self):
        print(self.x, " ", self.y)