


M = int(input("Quantas linhas vai ter a matriz? "))
N = int(input("Quantas colunas vai ter a matriz "))

mat: [[int]] = [[0 for x in range(N)] for x in range(M)]

for i in range(0, M): # para percorrer as linhas
    for j in range(0, N): # para percorrer as colunas
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))# (f) placeholder

print()
print("MATRIZ DIGITADA:")
for i in range (0, M):
    for j in range (0, N):
        print(f"{mat[i][j]} ", end="") # Você pode usar end="" para evitar a quebra de linha ou especificar outros caracteres para serem impressos no final, como espaços ou símbolos.
    print()

