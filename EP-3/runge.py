import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Função original
def f(x):
    return 1 / (1 + 25 * x**2)

# Função de erro máximo (||f(z) - p(z)||∞)
def calcular_erro(f_values, p_values):
    return np.max(np.abs(f_values - p_values))

# Divisão do intervalo
def divisao_do_intervalo(a, b, N):
    total = b - a
    distancia = total / N
    x_vals = np.zeros(N + 1)
    x_vals[0], x_vals[N] = a, b
    for i in range(1, N):
        x_vals[i] = x_vals[i - 1] + distancia
    return x_vals

# Interpolação linear usando interp1d
def interpolacao_spline_linear(x_vals, y_vals, z_vals):
    spline = interp1d(x_vals, y_vals, kind='linear')
    p_vals = spline(z_vals)
    return p_vals

# Interpolação cúbica usando interp1d
def interpolacao_spline_cubica(x_vals, y_vals, z_vals):
    spline = interp1d(x_vals, y_vals, kind='cubic')
    p_vals = spline(z_vals)
    return p_vals

# Interpolação polinomial
def polin(x, c):
    y = c[0]
    n = len(c)
    for i in range(1, n):
        y += c[i] * x**i
    return y

# Função para plotar os gráficos
def graph(x, y, xx, yy, N, method):
    plt.figure()
    plt.title(f"Gráfico de {method} para N = {N}")
    plt.plot(x, y, "o", label="Dados")
    plt.plot(xx, yy, label=f"{method}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.savefig(f'Grafico de {method} para N = {N}.png')
    plt.show()

# Função principal
def main():
    N_values = [5, 10, 20]
    a, b = -5, 5
    for N in N_values:
        x_vals = divisao_do_intervalo(a, b, N)
        y_vals = np.array([f(x) for x in x_vals])

        # Calcular os valores para as interpolação
        h = (b - a) / 50
        z = [a + h * i for i in range(51)]  # 51 pontos de amostragem
        f_values = np.array([f(z[i]) for i in range(51)])

        # Interpolação polinomial
        A = np.zeros((N + 1, N + 1))  # matriz A
        for j in range(N + 1):
            for i in range(N + 1):
                A[i][j] = x_vals[i]**j
        c = np.linalg.solve(A, y_vals)
        p_values_poly = np.array([polin(z[i], c) for i in range(51)])

        # Interpolação spline linear (função própria usando interp1d)
        p_values_linear = interpolacao_spline_linear(x_vals, y_vals, z)

        # Interpolação spline cúbica (função própria usando interp1d)
        p_values_cubica = interpolacao_spline_cubica(x_vals, y_vals, z)

        # Calcular os erros
        erro_max_poly = calcular_erro(f_values, p_values_poly)
        erro_max_linear = calcular_erro(f_values, p_values_linear)
        erro_max_cubica = calcular_erro(f_values, p_values_cubica)

        print(f"Erro máximo para polinômio (N = {N}): {erro_max_poly}")
        print(f"Erro máximo para spline linear (n = {N}): {erro_max_linear}")
        print(f"Erro máximo para spline cúbica (n = {N}): {erro_max_cubica}")
        print()

        # Gráficos para cada tipo de interpolação
        graph(x_vals, y_vals, z, p_values_poly, N, method="Polinômio")
        graph(x_vals, y_vals, z, p_values_linear, N, method="Spline Linear")
        graph(x_vals, y_vals, z, p_values_cubica, N, method="Spline Cúbica")

if '__main__' == __name__:
    main()