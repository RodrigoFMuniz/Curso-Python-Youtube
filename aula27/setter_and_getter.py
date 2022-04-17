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

p1 = Person('Rodrigo','Muniz')
p2 = Person('Fernando','Muniz')

print(p1.name)
print(p2.name)