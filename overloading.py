class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Name is {} and age is {}".format(name,age))
class teacher(person):
    def __init__(self,name,age,sub):
        person.__init__(self,name,age)
        self.sub=sub
        return(person.__str__(self)+"sub: {}".format(sub))
