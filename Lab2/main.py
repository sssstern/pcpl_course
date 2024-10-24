from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square



def main():
    N=21

    r = Rectangle(N, N, "blue")
    c = Circle(N, "green")
    s = Square(N, "red")
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()