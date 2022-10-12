'''
0,1,1,2,3,5,8,13, ...

fib1() retorna falha de recursão
RecursionError: maximum recursion depth exceeded

fib2(): Apresenta falha para valores de n muito grandes, por conta da PG de operações recursivas
fib3(): Utiliza um objeto do tipo memo para ganhar desempenho
fib4(): Utiliza lru_cache annotation
'''
from typing import Dict
from functools import lru_cache

# def fib1(n:int)->int:
#     return fib1(n-1)+fib1(n-2)

# def fib2(n:int)->int:
#     if n<2:
#         return n
#     return fib2(n-2)+ fib2(n-1)


# memo: Dict[int, int] = {0:0, 1:1}

# def fib3(n:int)->int:
#     if n not in memo:
#         memo[n] = fib3(n-2) + fib3(n-1)
#     return memo[n]

@lru_cache(maxsize=None)
def fib4(n:int)->int:
    if n<2:
        return n
    return fib4(n-2)+ fib4(n-1)

if __name__== "__main__":
    print(fib4(9))
    # print(__doc__)