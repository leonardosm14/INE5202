import numpy as np

#Aproximando raizes para f(x) = x²-5
def f(x):
    return x**2 - 5

#x raiz da reta
def raiz_da_reta(a,b):
    return (a*f(b) - b*f(a))/(f(b) - f(a))

def main():
    #intervalo inicial [a, b]
    a = 2
    b = 3

    #criterios
    tolerancia = 1.0e-6
    #número de interações
    i = 1
    imax = 100
    
    x = raiz_da_reta(a,b)

    while(abs(f(x))> tolerancia and i < imax):

        if f(a)*f(x) > 0:
            a = x
        else:
            b = x

        x = raiz_da_reta(a,b)
        i += 1

    print(x, abs(b-a)/2)

    #Como sabemos que o valor da raíz é sqrt(5), podemos calcular o erro
    print(f"Erro: {abs(np.sqrt(5) - x)}")

main()