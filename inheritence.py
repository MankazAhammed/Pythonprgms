class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("The name is {} and age is {}".format(name,age))
class teacher(person):
    def print(self,name,age):
        person.__init__(name,age)
