import numpy as np

# Divisão do intervalo
def divisao_do_intervalo(a, b, n):
    total = b - a
    distancia = total / n
    intervalo = np.zeros(n + 1)
    intervalo[0], intervalo[n] = a, b
    for i in range(1, n):
        intervalo[i] = intervalo[i - 1] + distancia
    return intervalo

def erro(integral):
    return np.abs(np.log(2) - integral)

def f(x):
    return 1/x

def retangulos(a, b, x, n):
    soma = 0
    h = (b-a)/n

    for i in range(n+1):
        soma += f(x[i])

    integral = h*soma
    return integral

def main():
    a, b = 1, 2
    n = 16 # divisão dos intervalos
    x = divisao_do_intervalo(a, b, n)
    print(x)
    integral = retangulos(a, b, x, n)
    err = erro(integral)
    print(f'Integral: {integral}, Erro: {err}')

if __name__ == '__main__':
    main()