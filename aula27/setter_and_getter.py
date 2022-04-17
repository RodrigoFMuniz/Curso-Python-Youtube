class Person:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self.__amigos = []
    
    @property
    def name(self):
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    @name.setter
    def name(self, name):
        self.__name = name

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

p1 = Person('Rodrigo','Muniz')
p2 = Person('Fernando','Muniz')

print(p1.name)
print(p2.name)
print(p1.surname)
print(p2.surname)
p1.name = "RODRIGO"
p1.surname = "Fernandes Muniz"
p2.name = "FERNANDO"
p2.surname = "Fernandes Muniz"
print(p1.name)
print(p2.name)
print(p1.surname)
print(p2.surname)