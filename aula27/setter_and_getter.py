class Person:
    def __init__(self, name, surname):
        self.__name = name.lower().capitalize()
        self.__surname = surname.lower().capitalize()
        self.__amigos = []
    
    @property
    def name(self):
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    @name.setter
    def name(self, name):
        self.__name = name.lower().capitalize()

    @surname.setter
    def surname(self, surname):
        self.__surname = surname.lower().capitalize()
    
    @property
    def amigos(self):
        return self.__amigos
    
    @amigos.setter
    def amigos(self,amigo):
        self.__amigos.append(amigo)
    
    def add_amigos(self, amigos=[]):
        if len(amigos) > 0:
            for a in amigos:
                self.__amigos.append(a.lower().capitalize())
    # def add_amigos(self, amigos=[]):
    #     if len(amigos) > 0:
    #         self.__amigos.extend(amigos)
    
    def remove_amigo(self, amigo):
        try:
            self.__amigos.remove(amigo)
        except:
            print(f'Valor {amigo} não existe na lista')
        
        

p1 = Person('RoDrIgo','MuNIz')
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
p1.amigos = 'Jéssica'
print(p1.amigos)
p1.add_amigos(['Cacau', 'RoBERto', 'Silvia'])
print(p1.amigos)
p1.remove_amigo('Roberto')
print(p1.amigos)
p1.remove_amigo('ggg')
print(p1.amigos)