import numpy as np

def f(x):
    return np.exp(x) - x - 1

def df(x):
    return np.exp(x) - 1

def main():
    x0 = 1

    #condicoes
    it = 1
    itmax = 100
    tol = 1.0e-6
    erro = 1

    while (erro > tol and it < itmax):
        x = x0 - f(x0)/df(x0)
        erro = abs(x-x0)
        x0 = x
        print(it, x, erro, abs(f(x)))
        it += 1

#main()