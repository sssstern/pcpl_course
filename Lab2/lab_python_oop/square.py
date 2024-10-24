from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    figure_type="square"

    def __init__(self, side_size, color):
        self.side_size=side_size
        super().__init__(side_size, side_size, color)

    @classmethod
    def get_figure_type(cls): return cls.figure_type
    def __repr__(self): return 'figure: {}; side: {}; color: {}; square: {};'.format(
        Square.get_figure_type(),self.side_size,
        self.fc.colorproperty,self.square()
    )