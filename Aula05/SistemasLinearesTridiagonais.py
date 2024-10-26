import numpy as np
import matplotlib.pyplot as plt

def vetores(N, T0, TN):
    '''
    d = diagonal principal
    a = diagonal abaixo da principal
    c = diagonal acima da principal 
    b = diagonal de solução
    '''

    a = [-1]*(N-1)

    #Já que T[0] = 0 e T[N-1] = 50:
    b = [T0]*(N)
    b[-1] = TN
    
    d = [2]*(N) 
    c = a

    return a, b, c, d


def matrix_tridiagonal(N):

    a, b, c, d = vetores(N, 0, 50)

    for i in range(N-1):
        m = a[i] / d[i]
        d[i+1] -= m * c[i]
        b[i+1] -= m * b[i]
    
    x = [0] * (N) 
    x[-1] = b[-1] / d[-1]  

    for i in range(N-2, -1, -1): 
        x[i] = (b[i] - c[i] * x[i+1]) / d[i]

    return x

def graph(N, x):
    plt.plot(range(0, N), x, marker='o', linestyle='-', color ='red')
    plt.title('Temperatura')
    plt.xlabel('Partições')
    plt.ylabel('Temperatura (°C)')
    plt.grid(True)
    plt.show()

def main():
    N_values = [5, 10, 20]
    for N in N_values:
        x = matrix_tridiagonal(N)
        print(len(x))
        h = (x[-1] - x[0]) / (N)
        print(f"x: {x}, h {h}")
        graph(N, x)

main()