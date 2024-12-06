import numpy as np

def f(ti, yi):
    return - ti*yi

def divisao_do_intervalo(a, b, N):
    total = b - a
    distancia = total / N
    x_vals = np.zeros(N + 1)
    x_vals[0], x_vals[N] = a, b
    for i in range(1, N):
        x_vals[i] = x_vals[i - 1] + distancia
    return x_vals

def Euler(y, t, delta_t):

    n = len(y)
    for i in range(1, n):
        y[i] = y[i-1] + delta_t * f(t[i-1], y[i-1])
    
    return y

if __name__ == '__main__':
    N = 4
    t = divisao_do_intervalo(0, 1, N)
    y = np.zeros(N)
    y[0] = 1
    delta_t = 1/N
    euler = Euler(y, t, delta_t)
    print(euler)