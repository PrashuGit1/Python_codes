class Circle:
    def draw(self):
        return "Drawing a Circle"

class Square:
    def draw(self):
        return "Drawing a Square"

class ShapeFactory:
    @classmethod
    def get_shape(cls, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError("Unknown shape type")
        
shape1 = ShapeFactory.get_shape("circle")
print(shape1.draw())  # Drawing a Circle

shape2 = ShapeFactory.get_shape("square")
print(shape2.draw())  # Drawing a Square

