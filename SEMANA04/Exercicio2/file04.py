

class Dog:
    def add_one(self,x):
        return x+1
    def meow(self):
        return "meow"
    def bark(self):
        print("bark")

d=Dog()
d.bark()
print(d.add_one(5))
print(type(d))


