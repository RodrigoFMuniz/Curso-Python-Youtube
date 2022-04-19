def sum(*v):
    if len(v)==0:
        return f"Entre com um valor"
    else:
        total = 0
        for num in v:
            if isinstance(num, float):
                total+=num
            elif isinstance(num, int):
                n = float(num)
                total+=n
            elif isinstance(num, str):
                if num.isnumeric():
                    n = float(num)
                    total+=n
                else:
                    pass
        return total


                
s = sum(1,2,'3', 4.6)
d = sum()
print(s)
print(d)


