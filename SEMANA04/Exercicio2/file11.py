class Pet:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f"i am {self.name} and i am {self.age} years old")
    def speak (self):
        print("i dont know what i say")

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color
    def speak(self):
        print("Meow")
    def show(self):
        print(f"i am {self.name} and i am {self.age} years old and i am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Tim",19)
p.speak()
p.show()
c=Cat("Bill",34,brown)
c.speak()
d=Dog("Jim",35)
d.speak()
d=Dog("Bob",10)
f.speak()
