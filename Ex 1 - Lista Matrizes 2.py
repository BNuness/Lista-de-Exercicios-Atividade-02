matriza  = [[2, 1], [-3, 4]]
matrizb  = [[0, -1], [2, 5]]
matrizc  = [[3, 0], [6, 1]]
matrizresult  = [[0, 0], [0, 0]]


matrizct= list(map(list, zip(*matrizc)))
print('Matriz A')
print('=-'* 8)
for j in matriza:
    print(j)
print()

print('Matriz B')
print('=-'* 8)
for j in matrizb:
    print(j)
print()

print('Matriz C')
print('=-'* 8)
for j in matrizc:
    print(j)
print()

for l in range(2):

    for c in range(2):
        matrizresult[l][c] = matrizb[l][c] - matrizct[l][c]

for l in range(2):

    for c in range(2):
        matrizresult[l][c] = matriza[l][c] + matrizresult[l][c]

for l in range(2):

    for c in range(2):
        matrizresult[l][c] = matrizresult[l][c] * matrizb[l][c]

print()
print('Resultado Cálculo: Matriz [A + (B-C^T)] * B =')
print('=-'* 8)
for l in  range (2):
    for c in range(2):
        print(f'[{matrizresult[l][c]:^5}]', end='')

    print()
print('=-'* 8)