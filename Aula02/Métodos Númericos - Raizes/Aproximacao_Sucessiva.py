import numpy as np
import matplotlib.pyplot as plt

#f(x) = x²+0.96x-2.08
def f(x):
    return x**2 + 0.96*x - 2.08

#sequência de funções phi para verificar convergências
def phi_1(x):
    return (2.08 - x**2) / 0.96

def phi_2(x):
    return (2.08) / (x+ 0.96)

def phi_3(x):
    return np.sqrt(2.08 - 0.96*x)

def phi_4(x):
    return (2.08+x**2) / (2*x+0.96)

def main():

    # Primeira parte
    #gráfico
    x = np.linspace(0, 2, 100)
    plt.plot(x, f(x), label = "$f(x)$")
    plt.plot(x, x, "--", label = "$y = x$")
    plt.plot(x, phi_4(x), label = "$phi(x)$")
    plt.grid()
    plt.legend(loc = "best")

    #iterações
    x0 = 1.5
    n_iter = 4
    for i in range(n_iter):
        x = phi_4(x0)
        plt.arrow(x0, x0, 0, x - x0)
        plt.arrow(x0, x, x-x0, 0)
        x0 = x 
        print(x)
    
    plt.savefig('plt_phi_4.png')

main()
    