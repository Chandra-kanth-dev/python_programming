from abc import ABC,abstractmethod
from math import pi
class Shape:
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print( self.length*self.breadth)
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
       print((22/7)*self.radius*self.radius)
rec = Rectangle(23,1)
rec.area()
cir = Circle(7)
cir.area()    
    