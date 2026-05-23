class Developer:
    def __init__(self, name, prog, experience=5):
        self.name = name                                            # public attribute
        self._prog = prog                                           # protected attribute
        self.__experience = experience                              # Private attribute


    def exp(self):
        return self.__experience
developer1 = Developer("Alice", "Python")
print(developer1.name)
print(developer1._prog)
                                                                                                                             
print(developer1.exp())    
print(developer1.__experience)                             # Accessing private attribute  directly will raise an AttributeError

print(developer1._Developer__experience)                                    # Accessing private attribute using name mangling