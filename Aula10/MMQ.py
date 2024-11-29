import numpy as np
import matplotlib.pyplot as plt

#Função aproximadora - reta
def g(x, a):
    return a[0] * x + a[1]

#Função resíduo
def residuo(a, x, y):
    return g(x, a) - y

def MMQ(xi, yi, p):

    n = len(xi) #tamanho das tabelas
    v1 = np.ones(n) #matriz de uns

    A = np.zeros((p, p)) #p = 2 - parametros da função aproximadora
    b = np.zeros(p)

    A[0][0] = np.vdot(v1, v1) # <1, 1> = 1*n
    A[0][1] = np.vdot(v1, xi)
    A[1][0] = A[0][1]
    A[1][1] = np.vdot(xi, xi)

    b[0] = np.vdot(v1, yi)
    b[1] = np.vdot(xi, yi)

    a = np.linalg.solve(A, b)
    print(f'a: {a}')
    
    #residuo
    res = 0
    for i in range(n):
        res += residuo(a, xi[i], yi[i])**2
    print(f'resíduo: {res}')

    x = np.linspace(xi[0], xi[-1], 100) #aumentando espaço 
    y = g(x, a)

    # Gráfico

    plt.figure(1)
    plt.plot(xi, yi, 'o', label='$y_i$')
    plt.plot(x, y, label='$g(x)$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

def main():

    xi = np.array([0, 0.25, 0.5, 0.75, 1])
    yi = np.array([1, 1.2480, 1.6487, 2.1170, 2.7183])

    MMQ(xi, yi, 2)

main()
