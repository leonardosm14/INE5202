import numpy as np
from NewtonComSegundaDerivada import *

def main():
    x0 = 1
    it = 1
    itmax = 100
    tol = 1.0e-6
    erro = 1

    while (erro > tol and it < itmax):
        x = x0 - df(x0) / ddf(x0)
        erro = abs(x - x0)
        x0 = x
        print(it, x, erro, abs(f(x)))
        it += 1
    
main()