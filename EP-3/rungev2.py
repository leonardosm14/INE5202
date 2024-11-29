import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Função original
def f(x):
    return 1 / (1 + 25 * x**2)


# Função de erro máximo (||f(z) - p(z)||∞)
def erro_maximo(f_values, p_values):
    return np.max(np.abs(f_values - p_values))

# Divisão do intervalo
def divisao_do_intervalo(a, b, n):
    total = b - a
    distancia = total / n
    intervalo = np.zeros(n + 1)
    intervalo[0], intervalo[n] = a, b
    for i in range(1, n):
        intervalo[i] = intervalo[i - 1] + distancia
    return intervalo

# Interpolação polinomial
def polin(x, c):
    y = c[0]
    n = len(c)
    for i in range(1, n):
        y += c[i] * x**i
    return y

# Função de erro
def calcular_erro(f_values, p_values):
    erro_max = erro_maximo(f_values, p_values)
    return erro_max

# Função para plotar os gráficos
def graph(x, y, xx, yy, n, method):
    plt.figure()
    plt.title(f"Gráfico de {method} para n = {n}")
    plt.plot(x, y, "o", label="Dados")
    plt.plot(xx, yy, label=f"{method}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()

# Função principal
def main():
    N = [5, 10, 20]
    a, b = -5, 5
    for n in N:
        x_vals = divisao_do_intervalo(a, b, n)
        y_vals = np.array([f(x) for x in x_vals])

        # Interpolação polinomial
        A = np.zeros((n + 1, n + 1))  # matriz A
        for j in range(n + 1):
            for i in range(n + 1):
                A[i][j] = x_vals[i]**j
        c = np.linalg.solve(A, y_vals)

        # Calcular os valores para as interpolação
        h = (b - a) / 50
        z = [a + h * i for i in range(51)]  # 51 pontos de amostragem
        f_values = np.array([f(z[i]) for i in range(51)])

        # Interpolação polinomial
        p_values_poly = np.array([polin(z[i], c) for i in range(51)])

        # Interpolação spline linear (usando interp1d)
        p_values_linear = np.array([interp1d(x_vals, y_vals, kind='linear')(z[i]) for i in range(51)])

        # Interpolação spline cúbica (usando interp1d)
        p_values_cubica = np.array([interp1d(x_vals, y_vals, kind='cubic')(z[i]) for i in range(51)])

        # Calcular os erros
        erro_max_poly, erro_norma_poly = calcular_erro(f_values, p_values_poly)
        erro_max_linear, erro_norma_linear = calcular_erro(f_values, p_values_linear)
        erro_max_cubica, erro_norma_cubica = calcular_erro(f_values, p_values_cubica)

        print(f"Erro máximo para polinômio (n={n}): {erro_max_poly}")
        print(f"Erro máximo (norma) para polinômio (n={n}): {erro_norma_poly}")
        print()
        print(f"Erro máximo para spline linear (n={n}): {erro_max_linear}")
        print(f"Erro máximo (norma) para spline linear (n={n}): {erro_norma_linear}")
        print()
        print(f"Erro máximo para spline cúbica (n={n}): {erro_max_cubica}")
        print(f"Erro máximo (norma) para spline cúbica (n={n}): {erro_norma_cubica}")
        print()

        # Gráficos para cada tipo de interpolação
        graph(x_vals, y_vals, z, p_values_poly, n, method="Polinômio")
        graph(x_vals, y_vals, z, p_values_linear, n, method="Spline Linear")
        graph(x_vals, y_vals, z, p_values_cubica, n, method="Spline Cúbica")

main()
