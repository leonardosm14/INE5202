import numpy as np
import cmath
import matplotlib.pyplot as plt

# p(x) = x⁴−3x³+x²+x+1

def f(x):
    return x**4 - 3*(x**3) + x**2 + x +1

def graph():
    x = np.linspace(0, 3, 200)
    y = f(x)
    plt.plot(x, y, label="f(x)")
    plt.title("Gráfico")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

def coeficientes(x0, x1, x2):
    q0 = (f(x0) - f(x2)) / (x0 - x2)
    q1 = (f(x1) - f(x2)) / (x1 - x2)

    a = (q0 - q1) / (x0 - x1)
    b = (q0*(x2-x1)+q1*(x0-x2)) / (x0 - x1)
    c = f(x2)

    return a, b, c

def proxima_aproximacao(x2, a, b, c):
    sgn_b = b / abs(b)
    x3 = x2 - (2*c / (b + sgn_b*cmath.sqrt(b**2-4*a*c)))
    return x3

def muller(x0, x1, x2):
    
    #Critérios de parada
    it = 1
    itmax = 100
    tol = 1.0e-6
    erro = 1

    a, b, c = coeficientes(x0, x1, x2)
    while (erro > tol and it < itmax):

        x3 = proxima_aproximacao(x2, a, b, c)
        
        erro = abs(x3 - x2)

        x0 = x1
        x1 = x2
        x2 = x3

        a, b, c = coeficientes(x0, x1, x2)
        print(f"Iterações: {it}, Erro: {erro}, X: {x2}, f(x): {abs(f(x2))}")
        it += 1
    
    return x2

def main():
    graph()
    '''
    Com o resultado do gráfico, observamos que há duas raízes reais:
    - No intervalo (1, 1.5) -> x0 = 1.1, x1 = 1.2, x2 = 1.3
    - No intervalo (2, 2.5) -> x0 = 2.1, x1 = 2.2, x2 = 2.3
    '''
    print('\nITERAÇÕES PARA ENCONTRAR A PRIMEIRA RAIZ REAL\n')
    raiz_real_1 = muller(x0 = 1.1, x1 = 1.2, x2 = 1.3)

    print('\nITERAÇÕES PARA ENCONTRAR A SEGUNDA RAIZ REAL\n')
    raiz_real_2 = muller(x0 = 2.1, x1 = 2.2, x2 = 2.3)

    #Primeira raiz complexa
    print('\nITERAÇÕES PARA ENCONTRAR A PRIMEIRA RAIZ COMPLEXA\n')
    raiz_complexa_1 = muller(x0 = -0.5, x1 = 0, x2 = 0.5)

    #Segunda raiz complexa: se a+bi é raiz, a-bi também é:
    raiz_complexa_2 = raiz_complexa_1.conjugate()

    print(f"\nPrimeira raiz real: {raiz_real_1} \nSegunda raiz real: {raiz_real_2} \nPrimeira raiz complexa: {raiz_complexa_1} \nSegunda raiz complexa: {raiz_complexa_2} ")
    
main()