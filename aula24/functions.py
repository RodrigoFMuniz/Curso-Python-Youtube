# functions
total = 0
def sum(*values):
    for n in values:
        total += n
    return total

values = [1,2,3,4,5,6,7,8,9,10]

# print(sum(values))
print(total)