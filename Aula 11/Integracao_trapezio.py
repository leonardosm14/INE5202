import numpy as np
from Integracao_retangulos import f, divisao_do_intervalo, erro

def trapezio(x, n):
    soma = 0
    h = (x[n] - x[0])/n
    
    for i in range(1, n):
        soma += f(x[i])

    integral = (h/2)*(2*soma + f(x[0]) + f(x[n]))

    return integral

def main():
    a, b = 1, 2
    n = 16 # divisão dos intervalos
    x = divisao_do_intervalo(a, b, n)
    print(x)
    integral = trapezio(x, n)
    err = erro(integral)
    print(f'Integral: {integral}, Erro: {err}')

if __name__ == '__main__':
    main()