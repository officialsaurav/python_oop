class car:
    def __init__(self,name,model,wheel):
        self.name=name
        self.model=model
        self.wheel=wheel
    def drive(self):
        return f"the {self.name} {self.model} is driving"



c1=car("hondai","i10",4)



print(c1.drive())
