generate a code to explain how different inherentance types work in Python.
# Inheritance is a fundamental concept in object-oriented programming that allows a new class (called a child or subclass) to inherit attributes and methods from an existing class (called a parent or superclass). In Python, there are several types of inheritance:
# 1. Single Inheritance: A child class inherits from a single parent class.
# 2. Multiple Inheritance: A child class inherits from more than one parent class.          

# 3. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class.
# 4. Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
# 5. Hybrid Inheritance: A combination of two or more types of inheritance.
# Here is an example to illustrate these types of inheritance:
# Single Inheritance
class Parent:
    def parent_method(self):
        return "This is the parent method." 
class Child(Parent):
    def child_method(self):
        return "This is the child method."




# Multiple Inheritance
class Parent1:          
    def parent1_method(self):
        return "This is the parent1 method."        
class Parent2:
    def parent2_method(self):
        return "This is the parent2 method."    
class ChildMultiple(Parent1, Parent2):
    def child_multiple_method(self):
        return "This is the child multiple method." 


# Multilevel Inheritance
class GrandParent:
    def grandparent_method(self):
        return "This is the grandparent method."
class ParentMultilevel(GrandParent):
    def parent_multilevel_method(self):
        return "This is the parent multilevel method."
class ChildMultilevel(ParentMultilevel):
    def child_multilevel_method(self):
        return "This is the child multilevel method."


# Hierarchical Inheritance
class ParentHierarchical:
    def parent_hierarchical_method(self):
        return "This is the parent hierarchical method."



class Child1(ParentHierarchical):
    def child1_method(self):
        return "This is the child1 method."
    


class Child2(ParentHierarchical):
    def child2_method(self):
        return "This is the child2 method." 
    
# Hybrid Inheritance    

class ParentHybrid1:

    def parent_hybrid1_method(self):
        return "This is the parent hybrid1 method."
class ParentHybrid2:        
    def parent_hybrid2_method(self):
        return "This is the parent hybrid2 method."     


class ChildHybrid(ParentHybrid1, ParentHybrid2):    
    def child_hybrid_method(self):
        return "This is the child hybrid method."






# Testing the classes
child_single = Child()
print(child_single.parent_method())
child_multiple = ChildMultiple()
print(child_multiple.parent1_method())


print(child_multiple.parent2_method())
child_multilevel = ChildMultilevel()            
print(child_multilevel.grandparent_method())            
print(child_multilevel.parent_multilevel_method())  
print(child_multilevel.child_multilevel_method())
child1 = Child1()   
print(child1.parent_hierarchical_method())
print(child1.child1_method())