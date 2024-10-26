import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def SOR(N, w):
    T = np.zeros((N+1, N+1))
    
    # Aplica a condição de contorno (bordas)
    for i in range(N+1):
        T[i][N] = 50  # Uma extremidade está a 50 graus
    
    # Definições para iteração
    num_iteracoes = 0
    itmax = int(1.0e4)
    residuo = 1
    tol = 1.0e-4

    # Iteração do método de SOR
    while (residuo > tol and num_iteracoes < itmax):
        T_old = T.copy()  # Copia a matriz antiga para cálculo do erro
        
        for i in range(1, N):
            for j in range(1, N):
                # Aplicação do método SOR
                soma_t = T[i-1][j] + T[i][j-1] + T[i+1][j] + T[i][j+1]
                T[i][j] = (1 - w) * T[i][j] + (w / 4) * soma_t
        
        # Calcula a diferença máxima entre a matriz nova e antiga
        residuo = np.max(np.abs(T - T_old))
        num_iteracoes += 1

    return T, num_iteracoes, residuo

# Função para plotar a distribuição de temperatura
def graph(N_values, df):
    plt.style.use('_mpl-gallery')

    for N in N_values:
        # Filtra o DataFrame para o valor atual de N
        df_N = df[df['N'] == N]
        
        # Encontra o w com o menor número de iterações
        w_opt = df_N.loc[df_N['Número de Iterações'].idxmin(), 'w']
        
        # Executa o método SOR com o w ótimo
        T_opt, it, residuo = SOR(N, w_opt)
        
        # Plota e salva o gráfico com um tamanho fixo de 6x6 polegadas
        fig, ax = plt.subplots(figsize=(6, 6))
        im = ax.imshow(T_opt, cmap='jet', extent=[0, 1, 0, 1])
        ax.set_title(f'Distribuição de Temperatura (N={N}, ω={w_opt:.1f})')
        fig.colorbar(im, ax=ax, label='Temperatura (°C)')
        plt.savefig(f'distribuicao_temperatura_N{N}_w{w_opt:.1f}.png')
        plt.close(fig)

# Função principal para calcular e registrar o número de iterações
def main():
    w_values = [k / 10 for k in range(1, 20)]  # Intervalo de ω no intervalo [0.1, 1.9]
    n_values = [10, 20, 40, 80]  # Valores de N
    data = []  # Vetor para armazenar os dados

    for N in n_values:
        for w in w_values:
            # Executa o método SOR e captura o número de iterações
            T, num_iteracoes, residuo = SOR(N, w)
            data.append([N, w, num_iteracoes, residuo])  # Adiciona os dados na lista
            print([N, w, num_iteracoes, residuo])

    # Cria um DataFrame com os resultados
    df = pd.DataFrame(data, columns=['N', 'w', 'Número de Iterações', 'Resíduo'])
    
    # Exibe o DataFrame
    print(df)

    # Salva o DataFrame em um arquivo CSV
    df.to_csv('comparacao_SORX.csv', index=False)

    # Gera os gráficos para cada valor de N com o w ótimo
    graph(n_values, df)
    
if __name__ == "__main__":
    main()
