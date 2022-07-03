import time as tm

# Basics about time
t1 = tm.time()
print(t1)

# gmtime
t2 = tm.gmtime(t1)
print(t2)

# Interval
antes = tm.time()
x = 0
for i in range(0, 10000):
    x += 1
depois = tm.time()

intervalo = depois - antes

print(f'{intervalo*1000} ms')
