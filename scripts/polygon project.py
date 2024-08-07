#Rectangle class to do some automate some basic computations for rectangles with integer lengths

class Rectangle:
    def __init__( self, width: int, height: int):
        self.width = width
        self.height = height
    def __repr__(self):
        return f"Rectangle(width=%s, height=%d)" % (self.width, self.height)
    def set_width(self, new_width: int):
        self.width = new_width
    def set_height(self, new_height: int):
        self.height = new_height

    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
        if self.width > 50 or self.height > 50:
          return 'Too big for picture.'
        line = '\n'.rjust(self.width+1,'*')
        result = ''
        for i in range(0, self.height):
           result += line
        return result
    def get_amount_inside(self, rectangle):
        num1 = self.height // rectangle.height
        num2 = self.width // rectangle.width
        return num1 * num2

    pass

#Square subclass inherits properties and methods of Rectangle class.
#Some methods are redefined to ensure reliable squareness.

class Square(Rectangle):
    def __init__(self, side: int):
        self.height = side
        self.width = side
    def __repr__(self):
        return "Square(side=%s)" % (self.height)
    
    def set_side(self, side: int):
        self.height = side
        self.width = side
    
    def set_width(self, side: int):
        self.height = side
        self.width = side

    def set_height(self, side: int):
        self.height = side
        self.width = side    

    pass

ba = Rectangle(4, 5)
print(ba.get_picture())
ab = Square(2)
print(ba.get_amount_inside(ab))
print(ba)
print(ab)