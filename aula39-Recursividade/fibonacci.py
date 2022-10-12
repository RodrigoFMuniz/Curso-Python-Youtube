'''
0,1,1,2,3,5,8,13, ...

fib1() retorna falha de recursão
RecursionError: maximum recursion depth exceeded

fib2(): Apresenta falha para valores de n muito grandes, por conta da PG de operações recursivas
'''
# def fib1(n:int)->int:
#     return fib1(n-1)+fib1(n-2)

def fib2(n:int)->int:
    if n<2:
        return n
    return fib2(n-1)+ fib2(n-2)

if __name__== "__main__":
    print(fib2(50))
    print(__doc__)