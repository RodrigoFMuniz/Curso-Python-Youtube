from main import sum

print(sum([1,2,3,4]))

if __name__ == "__main__":
    print(f'Chamou a função {sum.__name__} a partir do módulo importador.py, quando chamado em {__name__}')
