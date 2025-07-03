class Person():
# Định nghĩa lớp "name" 
    name = "Person"
    def __init__(self, name = None):
# self.name là biến instance 
        self.name = name

jeffrey = Person("Jeffrey")
print ("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print ("%s name is %s" % (Person.name, nico.name))
