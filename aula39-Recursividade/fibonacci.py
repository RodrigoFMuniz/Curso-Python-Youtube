'''
0,1,1,2,3,5,8,13, ...

fib1() retorna falha de recursão
RecursionError: maximum recursion depth exceeded
'''
def fib1(n:int)->int:
    return fib1(n-1)-fib1(n-2)
    

if __name__== "__main__":
    fib1(2)
    print(__doc__)