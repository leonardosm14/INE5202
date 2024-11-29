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

def Funcoes(variaveis): #variaveis (x, y)
    Fx = np.zeros(2)
    x, y = variaveis[0], variaveis[1] 
    
    Fx[0] = x**3 - 3*x*(y**2) - 1
    Fx[1] = 3*(x**2)*y - y**3

    return Fx

def Jacobiana(variaveis):
    x, y = variaveis[0], variaveis[1]
    J = np.zeros((2, 2))

    J[0][0] = 3*(x**2) - 3*(y**2)
    J[0][1] = -6*x*y   
    J[1][0] = 6*x*y
    J[1][1] = 3*(x**2) - 3*(y**2)

    return J

def Newton(variaveis):
    n = len(variaveis)
    solucoes = np.zeros(n)
    tol = 1.0e-6
    it, itmax = 1, 20
    residuo = 1

    while (residuo > tol and it < itmax): 
        F = Funcoes(variaveis)
        J = Jacobiana(variaveis)

        s = np.linalg.solve(J, -F)
        solucoes[:] = variaveis[:] + s[:]

        residuo = max_value(s)
        variaveis = np.copy(solucoes)
        
        it += 1

    return it #Para esse exercício, queremos apenas o número de iterações para convergência

def Regiao(N):
    x_vals = np.linspace(-1.5, 1.5, N)
    y_vals = np.linspace(-1.5, 1.5, N)
    C = np.zeros((N, N))
    
    for i in range(N):
        for j in range(N):
            p = np.array([x_vals[i], y_vals[j]])
            C[i][j] = Newton(p)
    
    return C

def graph(C, N):
    plt.imshow(C, extent=(-1.5, 1.5, -1.5, 1.5), origin='lower', cmap='viridis')
    plt.colorbar(label='Número de Iterações')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Região de Convergência do Método de Newton, N = {N}')
    plt.savefig('Região-Newton.png')
    plt.show()

# Função principal para executar o cálculo e plotar o mapa de convergência
def main():
    N = 200
    print("Delimitando a região...")
    C = Regiao(N)
    print("Gerando mapa de convergências...")
    graph(C, N)

if __name__ == '__main__':
    main()