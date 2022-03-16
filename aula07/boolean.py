from base64 import b16encode


b1 = False
b2 = True
 
print(type(b1))
print(type(b2))

print(b1)
print(b2)

print(b1.bit_count())
print(b2.bit_count())

print(str(b1))
print(str(b2))

b12s1 = str(b1)
b22s2 = str(b2)

print(type(b12s1))
print(type(b22s2))

print(b12s1.upper())
print(b22s2.lower())