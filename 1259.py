x = int(input())
lista = []
while x > 0:
    y = int(input())
    lista.append(y)
    x -=1

lista.sort()

listapar = []
listai = []
for i in lista:
    if i % 2 == 0:
        listapar.append(i)
    else:
        listai.append(i)

for i in listapar:
    print(i)

listai.reverse()

for i in listai:
    print(i)
