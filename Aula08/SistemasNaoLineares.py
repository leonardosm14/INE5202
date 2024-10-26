# Sistemas não linears com método de Newton
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def max_value(x):
    n = len(x)
    max_ = abs(x[0])
    for i in range(1, n):
        value = abs(x[i])
        if value > max_:
            max_ = value
    return max_

def F(x):
    n = len(x)
    Fx = np.zeros(n)

    Fx[0] = 2*x[0]**3 - x[1]**2-1
    Fx[1] = x[0]*x[1]**3 - x[1] - 4

    return Fx

def J(x):
    n = len(x)
    Jx = np.zeros((n, n))

    Jx[0][0] = 6*x[0]**2
    Jx[0][1] = -2*x[1]
    Jx[1][0] = x[1]**3
    Jx[1][1] = 3*x[0]*x[1]**2 - 1

    return Jx

def Newton(x0):
    n = len(x0)
    x = np.zeros(n)
    tol = 1.0e-6
    it, itmax = 1, 100
    dif = 1

    while (dif > tol and it < itmax): 
        Fx = F(x0)
        Jx = J(x0)
        s = np.linalg.solve(Jx, -Fx)
        x[:] = x0[:] + s[:]
        dif = max_value(s)
        x0 = np.copy(x)
        print(it, dif, x)
        it += 1

    return x

def main():
    x0 = np.array([1.2, 1.7])
    x = Newton(x0)

main()