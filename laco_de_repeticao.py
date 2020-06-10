# -*- coding: utf-8 -*-
x = 1

while x < 10:
    print(x)
    x = x + 1 # ou x += 1

# conceito de variável lista
lista1 = [1,2,3,4,5,6]
lista2 = ["eu","estou","quebrado"]
lista3 = [6,6.45,"Coringa é rei",True]

for i in lista1:
    print(i)
for i in lista2:
    print(i)
for i in lista3:
    print(i)

# comando "for" e "range"
for i in range(3):
    print(i)