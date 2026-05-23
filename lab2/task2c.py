#c. Create a Python class named Point that accepts x and y coordinates. 
# Program it so that it mathematically adds the coordinates together.


class Point:
   def __init__(self,x,y):
      self.x=x
      self.y=y



#getting user input coordinates

a1=int(input("Enter the x coordinate of point 1: "))
b1=int(input("Enter the y coordinate of point 1: "))
a2=int(input("Enter the x coordinate of point 2: "))
b2=int(input("Enter the y coordinate of point 2: "))


#objects

p1=Point(a1,b1)
p2=Point(a2,b2)
p=Point(p1.x+p2.x,p1.y+p2.y)
print (f"the coordinate is{p.x} , {p.y}")
