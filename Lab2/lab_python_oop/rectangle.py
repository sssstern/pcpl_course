from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor

class Rectangle(Figure):
    figure_type="rectangle"

    def __init__(self, width, heigth, color):
        self.width=width
        self.heigth=heigth
        self.fc = FigureColor()
        self.fc.colorproperty = color

    @classmethod
    def get_figure_type(cls):return cls.figure_type
    def square(self): return self.width*self.heigth
    def __repr__(self): return 'figure: {}; width: {}; height: {}; color: {}; square: {};'.format(
        Rectangle.get_figure_type(),
        self.width,self.heigth,
        self.fc.colorproperty,self.square()
    )

