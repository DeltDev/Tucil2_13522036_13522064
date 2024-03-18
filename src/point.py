#Objek titik

class Point:
    def __init__(self,x,y,pointName):
        self.x = x #nilai di koordinat x
        self.y = y #nilai di koordinat y
        self.pointName = pointName #nama titik (untuk keperluan visualisasi)
    def printPoint(self):
        print(self.x, " ", self.y," ",self.pointName)