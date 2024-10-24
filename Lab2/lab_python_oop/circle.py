import math
from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor

class Circle(Figure):
    figure_type="circle"

    def __init__(self, radius, color):
        self.radius=radius
        self.fc = FigureColor()
        self.fc.colorproperty = color
    @classmethod
    def get_figure_type(cls):return cls.figure_type
    def square(self): return math.pi*(self.radius**2)
    def __repr__(self): return 'figure: {}; radius: {}; color: {}; square: {};'.format(
        Circle.get_figure_type(),
        self.radius,self.fc.colorproperty,self.square()
    )
