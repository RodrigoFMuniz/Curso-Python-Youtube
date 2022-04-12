class Pessoa:
    def __init__(self):
        self._nome = None
    
    def __repr__(self):
        return self._nome

    def __str__(self):
        return self._nome
    
    def get_nome(self):
        return self._nome

    def set_name(self, nome):
        self._nome = nome

class Funcionario(Pessoa):
    def __init__(self):
        super().__init__(self)
        self.cargo = None



pessoa_1 = Pessoa()

print(pessoa_1._nome)
print(type(pessoa_1._nome))
print(pessoa_1.__repr__())
print(pessoa_1.__str__())

pessoa_1._nome='Rodrigo'

print(pessoa_1._nome)
print(type(pessoa_1._nome))
print(pessoa_1.__repr__())
print(pessoa_1.__str__())
print('Get:',pessoa_1.get_nome())
print('Set:', pessoa_1.set_name('Fernando'))
print('Get:',pessoa_1.get_nome())

func_1 = Funcionario()
func_1.cargo = 'Office boy'
func_1.set_name('Carlos')
print(func_1.get_nome())
print(func_1.cargo)