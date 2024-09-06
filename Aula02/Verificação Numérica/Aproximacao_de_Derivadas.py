import numpy as np
import math

e = math.e

def f(x):
    return x**2 + e**2

def df(x):
    return 2*x + e**2

def approximacao_derivada(x, h):
    dfx = (f(x+h) - f(x)) / h
    return dfx

def main():
    x0 = 1
    h = 0.5
    df = approximacao_derivada(x0, h)
    erro = abs(df - df(x0))
    print(erro)

main()
