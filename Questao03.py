import math


def calcularAreaCirculo(raio):
    area = math.pi * raio ** 2
    return area


def calcularAreaQuadrado(lado):
    area = lado ** 2
    return area


def calcularAreaRetangulo(base, altura):
    area = base * altura
    return area


continuarJogo = True

while continuarJogo:

    escolhaArea = int(input('Qual forma geométrica deseja calcular? Circulo [1], Quadrado [2], Retangulo [3]: '))

    if escolhaArea == 1:
        raio = float(input('Digite o tamanho do RAIO do círculo: '))
        print(calcularAreaCirculo(raio))

    elif escolhaArea == 2:
        lado = float(input('Digite o tamanho de um LADO do quadrado: '))
        print(calcularAreaQuadrado(lado))

    elif escolhaArea == 3:
        base = float(input('Digite o tamanho da BASE do retangulo: '))
        altura = float(input('Digite a ALTURA do retangulo: '))
        print(calcularAreaRetangulo(base, altura))

    else:
        print('Opcao inválida! Tente novamente.')

    continuar = int(input('Deseja continuar? Sim [1] ou Não [2]: '))

    if continuar == 1:
        continuarJogo

    else:
        break


