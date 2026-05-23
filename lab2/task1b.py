class Account:
    def __init__(self,id,amount,number):
        self.id=id
        self._amount=amount
        self.__number=number

    def num(self):
        return self.__number
    

a1=Account(101,2000,9876)
print(a1.id)
print(a1._amount)
print(a1.num())



print(a1.__number)




