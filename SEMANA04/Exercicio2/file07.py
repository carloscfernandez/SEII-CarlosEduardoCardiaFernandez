class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(name)
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age = age
d=Dog("Tim",34)
print(d.name)
d2=Dog("Bill",12)
print(d2.name)



