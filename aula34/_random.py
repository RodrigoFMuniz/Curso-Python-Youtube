import random

# basic about random
rd1 = random.random()
print(rd1)

# randint
rd2 = random.randint(1, 10)
print(rd2)

# randrange
rd3 = random.randrange(1, 40, 3)
print(rd3)

# Choice
x = [1, 2, 3, 1, 'e', 'tr', 'er-3', 34]
rd4 = random.choice(x)
print(rd4)

# Choices
x = [1, 2, 3, 1, 'e', 'tr', 'er-3', 34]
rd5 = random.choices(x, [1.0, 0.3, 0.2, 0.3, 0.2, 0.3, 0.2, 0.3])
print(rd5)
