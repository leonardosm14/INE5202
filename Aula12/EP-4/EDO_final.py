
'''
Problema 1:

Pelo método da Integração por Retângulos, sabemos que na divisão do intervalo
em N partes, teremos:

h = (b-a)/N
integral_a_b f(t, y)dt = h * [f(t[0], y[0]) + f(t[1], y[1]) + ... + f(t[N+1], y[N+1])]

Assim, o PVI: y(b) = y(a) + delta * \integral_a_b (f(t,y)dt), após repartir o intervalo [a, b] 
em N partes, será computado como:
 
(Assumindo h = delta)
y[b] = y[a] + delta * f(t[a], y[a])

Generalizando para N+1 pontos sucessivos:

y[i] = y[i-1] + delta * (f[t[i-1], y[i-1]]), que é o Método de Euler em questão.

Ou, ainda: y[i+1] = y[i] + delta * (f[t[i], y[i]])

Vamos optar por utilizar a primeira versão da fórmula para solução do problema.

'''

#Problema 2: Solução no código abaixo para N = [10, 20, 40]

import numpy as np
import matplotlib.pyplot as plt

def f(ti, yi):
    return -6*yi + 6

def erro_absoluto(ti, yi):
    yt = 1 + np.exp(-6*ti)  # Solução exata
    erro = abs(yi - yt)
    return erro

def divisao_do_intervalo(a, b, delta, N):
    T = np.zeros(N+1)
    T[0], T[N] = a, b
    for i in range(1, N):
        T[i] = a + i*delta
    return T

def Y_valores(delta, T, y0, N):
    Y = np.zeros(N+1)  # vetor de soluções y
    Y[0] = y0
    for i in range(1, N+1):
        Y[i] = Y[i-1] + delta * f(T[i-1], Y[i-1])
    return Y

def graph(T, Y, N):
    plt.figure(figsize=(8, 6))
    plt.plot(T, Y, marker='o', color='b', label='Solução de Y')
    plt.xlabel('T')
    plt.ylabel('Y')
    plt.title(f'Gráfico da Solução Y x T (Método de Euler), N = {N}')
    plt.grid(True)
    plt.legend()
    plt.savefig(f"Gráfico da Solução Y x T, N = {N}.png")
    plt.show()

if __name__ == '__main__':
    N_vals = [10, 20, 40]
    a, b = 0, 1
    y0 = 2  # PVI y(0) = 2

    for N in N_vals:
        
        delta = (b-a)/N
        T = divisao_do_intervalo(a, b, delta, N)
        Y = Y_valores(delta, T, y0, N)

        for i in range(N+1):
            ti, yi = T[i], Y[i]
            erro_abs = erro_absoluto(ti, yi)
            print(f"T[{i}] = {ti}, Y[{i}] = {yi}, Erro absoluto = {erro_abs}")

        #gráfico Y x T
        graph(T, Y, N)