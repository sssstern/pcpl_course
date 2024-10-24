import abc

class Figure(abc.ABC):
    @abc.abstractmethod 
    def square(self): pass 