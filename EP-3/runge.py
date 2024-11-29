import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Função original
def f(x):
    return 1 / (1 + 25 * x**2)

# Norma do erro
def norma(f, p):
    modulo = 0
    for i in range(len(f)):
        modulo += (f[i] - p[i])**2
    modulo = np.sqrt(modulo)
    return modulo

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

# Interpolação spline linear
def spline_linear(x, x_vals, y_vals):
    n = len(x_vals)
    for i in range(n - 1):
        x0, x1 = x_vals[i], x_vals[i + 1]
        y0, y1 = y_vals[i], y_vals[i + 1]
        if x0 <= x <= x1:
            fx = y0 * (x1 - x) / (x1 - x0) + y1 * (x - x0) / (x1 - x0)
            return fx

# Interpolação spline cúbica
def spline_cubica(x, x_vals, y_vals):
    cs = CubicSpline(x_vals, y_vals)
    return cs(x)

# Função de erro
def calcular_erro(a, b, n, x_vals, y_vals, c, tipo):
    h = (b - a) / 50
    z = [a + h * i for i in range(51)]  # Ajustado para 51 pontos (não n+1)
    
    f_values = np.array([f(z[i]) for i in range(51)])
    
    if tipo == 'polinomial':
        p_values = np.array([polin(z[i], c) for i in range(51)])
    elif tipo == 'linear':
        p_values = np.array([spline_linear(z[i], x_vals, y_vals) for i in range(51)])
    elif tipo == 'cubica':
        p_values = np.array([spline_cubica(z[i], x_vals, y_vals) for i in range(51)])
    
    erro_max = erro_maximo(f_values, p_values)
    return erro_max  # Apenas o erro máximo é retornado

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

        # Interpolação spline linear
        p_values_linear = np.array([spline_linear(z[i], x_vals, y_vals) for i in range(51)])

        # Interpolação spline cúbica
        p_values_cubica = np.array([spline_cubica(z[i], x_vals, y_vals) for i in range(51)])

        # Calcular os erros
        erro_max_poly = calcular_erro(a, b, n, x_vals, y_vals, c, tipo='polinomial')
        erro_max_linear = calcular_erro(a, b, n, x_vals, y_vals, c, tipo='linear')
        erro_max_cubica = calcular_erro(a, b, n, x_vals, y_vals, c, tipo='cubica')

        print(f"Erro máximo para polinômio (n={n}): {erro_max_poly}")
        print(f"Erro máximo para spline linear (n={n}): {erro_max_linear}")
        print(f"Erro máximo para spline cúbica (n={n}): {erro_max_cubica}")

        # Gráficos para cada tipo de interpolação
        graph(x_vals, y_vals, z, p_values_poly, n, method="Polinômio")
        graph(x_vals, y_vals, z, p_values_linear, n, method="Spline Linear")
        graph(x_vals, y_vals, z, p_values_cubica, n, method="Spline Cúbica")

main()
