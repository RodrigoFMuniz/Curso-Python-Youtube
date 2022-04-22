def sum(lista = []):
    total = 0
    for i in lista:
        total+= int(i)

if __name__ == "__main__":
    print(f'Chamou a função {sum.__name__}')
