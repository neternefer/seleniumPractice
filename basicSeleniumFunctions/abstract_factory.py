'''
Abstract Factory Design Pattern
- creating related objects without specifying their actual class
- used e.g. for hiding implementation details
'''
class Shape:

    def __init__(self, shape=None):
        self.shape_factory = shape

    def show_perimeter_formula(self):
        #self.shape_factory() creates an instance of passed in shape class -> e.g. Triangle
        #shape = self.shape_factory()
        print("{} perimeter = {}".format(self.shape_factory(), self.shape_factory().perimeter_formula()))

class Rectangle:

    def perimeter_formula(self):
        return "2 * (a + b)"

    def __str__(self):
        return "Rectangle"

class Triangle:

    def perimeter_formula(self):
        return "a + b + c"

    def __str__(self):
        return "Triangle"

    

if __name__ == "__main__":

    shapes = [Shape(Rectangle), Shape(Triangle)]
    for shape in shapes:
        shape.show_perimeter_formula()
        #shape class name is Shape, no mention of other classes used 
        print("My class name is: {}".format(shape.__class__.__name__))
