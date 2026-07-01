print("Circle")
radius = float(input("enter the radius of circle: "))
unit = input("enter the unit of circle: ")
class Circle:
    def __init__(self, radius, unit):
        self.radius = radius
        self.unit =  unit
    def show_radius(self):
        print("radius of circle is:",str(self.radius) + self.unit)
    def area(self):
        area = 3.14 *self.radius**2
        print("area of circle is:",str(area) + self.unit + "^2")
    def circumference(self):
        circumference = 2 * 3.14 * self.radius
        print("circumference of circle is:",str(circumference) + self.unit)
r = Circle(radius, unit)
r.show_radius()
r.area()
r.circumference()
