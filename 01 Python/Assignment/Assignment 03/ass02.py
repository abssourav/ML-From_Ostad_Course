'''
Create three classes Animal, Mammal, and Dog where Animal has a method eat(),
Mammal inherits from Animal and has a method walk(), and Dog inherits from Mammal and has a method bark().
Create an object of Dog and demonstrate all three methods. Also, create a class Calculator with an add()
method that can take either two or three parameters, and then create a subclass AdvancedCalculator that overrides 
the add() method to add any number of parameters using variable-length arguments. Demonstrate both functionalities.

'''


#Multilevel inheritance
class Animal:
    def eat(self):
        print("this is the eat method")

class Mammal(Animal):
    def walk(self):
        print("this is the walk method")

class Dog(Mammal):
    def bark(self):
        print("this is the bark method")

obj1 = Dog()
obj1.eat()
obj1.walk()
obj1.bark()





#normal vs adnvanced calculator
class Calculator:
    def add(self,a,b,c=0):      #method overloading
        print(a+b+c)

class AdvancedCalculator(Calculator):
    # def __init__(self):
    #     self.result = 0

    def add(self,*numbers):         #method overriding
        self.result = 0
        for number in numbers:
            self.result += number

        print(self.result)

add1 = Calculator()
add1.add(1,1)
add1.add(1,1,1)

add2 = AdvancedCalculator()
add2.add(1,1,1)
add2.add(1,1,1,1,1,1,1)