def sum(lista = []):
    total = 0
    for i in lista:
        total+= int(i)
    return total

if __name__ == "__main__":
    print(f'Chamou a função {sum.__name__} a partir do módulo main.py, quando chamado em {__name__}')
