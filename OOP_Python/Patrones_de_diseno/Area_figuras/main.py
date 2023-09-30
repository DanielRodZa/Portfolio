from abc import ABC, abstractmethod

class IShape(ABC):
    @abstractmethod
    def area(self) -> float: pass

class Tringle(IShape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return ((self.width * self.height) / 2)

class Rectangle(IShape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class Circle(IShape):
    def __init__(self, radio: float):
        self.radio = radio

    def area(self) -> float:
        return 3.1416 * (self.radio)**2

class IShapeFactory(ABC):
    @abstractmethod
    def get_shape(self, *args) -> IShape: pass

class TriangleFactory(IShapeFactory):
    def get_shape(self, width: float, height: float) -> IShape:
        return Tringle(width=width, height=height)

class RectagleFactory(IShapeFactory):
    def get_shape(self, width: float, height: float) -> IShape:
        return Rectangle(width=width, height=height)

class CircleFactory(IShapeFactory):
    def get_shape(self, radio: float) -> IShape:
        return Circle(radio=radio)

class AreaCalculator:
    @staticmethod
    def calc_area(shape: IShapeFactory, *args):
        """ Calcular el área de una figura específica """
        shape = shape().get_shape(*args)
        area = shape.area()
        return area

def read_factory() -> IShapeFactory:
    factories = {
        'rectangulo':RectagleFactory,
        'triangulo':TriangleFactory,
        'circulo':CircleFactory
    }
    while True:
        option = str(input('Ingrese la opcion que desea calcular (rectangulo, triangulo, circulo): '))
        if option in factories:
            return factories[option]
        print(f'Opcion no valida: {option}')

if __name__ == '__main__':
    factory = read_factory()
    a = AreaCalculator.calc_area(factory, 20)
    print(a)