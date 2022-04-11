class Pessoa:
    def __init__(self):
        self.nome = None
    
    def __repr__(self):
        return self.nome

    def __str__(self):
        return self.nome



pessoa_1 = Pessoa()

print(pessoa_1.nome)
print(type(pessoa_1.nome))
print(pessoa_1.__repr__())
print(pessoa_1.__str__())

pessoa_1.nome='Rodrigo'

print(pessoa_1.nome)
print(type(pessoa_1.nome))
print(pessoa_1.__repr__())
print(pessoa_1.__str__())