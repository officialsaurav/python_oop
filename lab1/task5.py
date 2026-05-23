class Student:
    def __init__(self,marks):
        self.marks=marks

    def show(self):
        print(self.__marks)

s=Student(90)
s.show

