matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

diagonalPrincipal = []

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para {l, c}: '))
        if l == c:
            diagonalPrincipal.append((matriz[l][c]))

for linha in matriz:
    print(linha)

print(sum(diagonalPrincipal))
print(max(diagonalPrincipal))
print(min(diagonalPrincipal))