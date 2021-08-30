matriza  = [[2, 1], [-3, 4]]
matrizb  = [[0, -1], [2, 5]]
matrizc  = [[3, 0], [6, 1]]
matrizresult  = [[0, 0], [0, 0]]
matrizci  = [[0, 0], [0, 0]]
matrizresultab  = [[0, 0], [0, 0]]
matrizresult3b  = [[0, 0], [0, 0]]


matrizat= list(map(list, zip(*matriza)))
print('Matriz A')
print('=-'* 8)
for j in matriza:
    print(j)
print()

matrizbt= list(map(list, zip(*matrizb)))
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

def det2(matrizc):
    return matrizc[0][0]*matrizc[1][1] - matrizc[0][1]*matrizc[1][0]

def inv2(matrizc):
    d = det2(matrizc)
    return [[matrizc[1][1]/d, -matrizc[0][1]/d], [-matrizc[1][0]/d, matrizc[0][0]/d]]

matrizci = inv2(matrizc)


for l in range(2):

    for c in range(2):
        matrizresultab[l][c] = matrizb[l][c] + matrizat[l][c]

for l in range(2):

    for c in range(2):
        matrizresult3b[l][c] = 3 * matrizbt[l][c]

for l in range(2):

    for c in range(2):
        matrizresult[l][c] = matrizresultab[l][c] * matrizci[l][c]

for l in range(2):

    for c in range(2):
        matrizresult[l][c] = matrizresult[l][c] - matrizresult3b[l][c]

print()
print('Resultado Cálculo: Matriz (B + A^T) * C^-1 -(3 * B^T)')
print('=-'* 8)
for l in  range (2):
    for c in range(2):
        print(f'[{matrizresult[l][c]:^5.2f}]', end='')
    print()
print('=-'* 8)
