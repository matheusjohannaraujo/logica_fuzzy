import math

def sigmoide(x, a, c):
    return  1 / (1 + math.exp(-a * (x - c)))

x = int(input("\r\n Digite o número de iteracoes: "))
a = int(input("\r\n Digite o intervalo de inicio: "))
c = int(input("\r\n Digite o intervalo final: "))

print("\r\n FUNCTION sigmoide(X, A, C)")
for i in range(x):
    print("\r\n Resultado da sigmoide(", i + 1, ",", a, ",", c, ") = ", sigmoide(i + 1, a, c))
