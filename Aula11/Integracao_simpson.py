import numpy as np
from Integracao_retangulos import f, divisao_do_intervalo, erro

def simpson(x, n):
    soma = 0
    h = (x[n] - x[0])/n

    for i in range(1, n, 2):
        soma += 2*f(x[i])+f(x[i+1])

    integral = (h/3) * (2*soma+f(x[0])-f(x[n]))
    return integral


def main():
    a, b = 1, 2
    n = 16 # divisão dos intervalos
    x = divisao_do_intervalo(a, b, n)
    print(x)
    integral = simpson(x, n)
    err = erro(integral)
    print(f'Integral: {integral}, Erro: {err}')
    

if __name__ == '__main__':
    main()