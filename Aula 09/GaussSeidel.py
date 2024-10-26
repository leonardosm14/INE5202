import numpy as np
import matplotlib.pyplot as plt


# Função Gauss-Seidel modificada para gerar a matriz T
def GaussSeidel(N):
    T = np.zeros((N+1, N+1))
    
    # Aplica a condição de contorno (bordas)
    for i in range(N+1):
        T[i][N] = 50  # Uma extremidade está a 50 graus
    
    # Definições para iteração
    it = 0
    itmax = 1.0e4
    dif = 1
    tol = 1.0e-4

    # Iteração do método de Gauss-Seidel
    while dif > tol and it < itmax:
        T_old = T.copy()  # Copia a matriz antiga para cálculo do erro
        
        for i in range(1, N):
            for j in range(1, N):
                T[i][j] = (T[i-1][j] + T[i][j-1] + T[i+1][j] + T[i][j+1]) / 4
        
        # Calcula a diferença máxima entre a matriz nova e antiga
        dif = np.max(np.abs(T - T_old))
        it += 1

    return T

# Função para plotar a distribuição de temperatura
def graph(T):
    plt.style.use('_mpl-gallery')
    fig, ax = plt.subplots()
    im = ax.imshow(T, cmap='jet', extent=[0, 1, 0, 1])
    ax.set_title('Distribuição de Temperatura')
    fig.colorbar(im, ax=ax, label='Temperatura (°C)')
    plt.show()

# Função principal
def main():
    N = 5  # Tamanho da malha
    w = 1.1  # Parâmetro de relaxação

    # Resolve o sistema usando Gauss-Seidel para gerar a matriz T
    T = GaussSeidel(N)
    print(T)
    print("Resultado Gauss-Seidel")
    graph(T)


main()
