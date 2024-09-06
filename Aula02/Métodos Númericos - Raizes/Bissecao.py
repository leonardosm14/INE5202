import numpy as np

#Aproximando raizes para f(x) = x²-5
def f(x):
    return x**2 - 5

def ponto_medio(a, b):
    return (a + b) / 2

def main():
    #intervalo inicial [a, b]
    a = 2
    b = 3

    #criterios
    tolerancia = 1.0e-6
    #número de interações
    i = 1
    imax = 100
    
    x_medio = ponto_medio(a, b)
    while(abs(b-a)/2 > tolerancia and i < imax):

        if f(a)*f(x_medio) > 0:
            a = x_medio
        else:
            b = x_medio

        x_medio = ponto_medio(a, b)
        i += 1

    print(x_medio, abs(b-a)/2)

    #Como sabemos que o valor da raíz é sqrt(5), podemos calcular o erro
    print(f"Erro: {abs(np.sqrt(5) - x_medio)}")

main()