listaInteiros = list()


def retornaListaPares(lista):
    listaPares =[]
    for n in lista:
        if n % 2 == 0:
            listaPares.append(n)
    return listaPares


def retornaListaImpares(lista):
    listaImpares = []
    for n in lista:
        if n % 2 != 0:
            listaImpares.append(n)
    return listaImpares


for v in range(10):
    valor = int(input('Digite um valor: '))
    listaInteiros.append(valor)


print('\n NÚMEROS PARES')
for p in (retornaListaPares(listaInteiros)):
    print(p)

print('=-' * 10)

print('\n NÚMEROS ÍMPARES')
for i in (retornaListaImpares(listaInteiros)):
    print(i)