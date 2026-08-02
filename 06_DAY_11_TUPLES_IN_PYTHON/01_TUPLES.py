a = (2 , 23 , 23 , 24.78 , "Aman" , "Kumar" , True , "Aman" , "Aman" ,1)
print(type(a))

i = a.count(23)
print(i)

j = a.count("Aman")
print(j)

k = a.index("Aman")
print(k)

l = a.index(True)
print(l)

print(len(a))

print("Aman" in a)
print(False in a)
print(a[0:3])

b = ( 1 , 2 , 4 , 56 , 65)
c = (65 , 2 , 23 , 56 )

d = b + c
print(d)

print(len(d))

print( 2 in b)
print(3 in b)
print(c[1:])
print(b[0:])

a , b , c , d = c
print(a , b , c , )
