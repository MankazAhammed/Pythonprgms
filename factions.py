class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("welcome {}".format(name))
    def __str__(self):
        print("name: {}\nage: {}".format(name,age))
    
    def __del__(self):
        print("Memory alloction is deleted as {} is dead".format(name))
        
p1=person("peter",21)
p2=person('minnu',20)
print(p1)
print(p2)
del(p1)
del(p2)
