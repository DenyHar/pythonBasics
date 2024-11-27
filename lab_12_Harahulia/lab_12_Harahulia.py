import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getxy(self):
        return  [self.__x, self.__y]

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__A = vertice1
        self.__B = vertice2
        self.__C = vertice3

    def perimeter(self):
        sum = math.dist(self.__A.getxy(),self.__B.getxy())
        sum += math.dist(self.__A.getxy(), self.__C.getxy())
        sum += math.dist(self.__B.getxy(), self.__C.getxy())
        return sum

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())