class cicle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2
    def circumference(self):
        return 2*3.14*self.radius   

my_circle=cicle(5)
print("Area of the circle:",my_circle.area())