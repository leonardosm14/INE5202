import numpy as np

def matrix():
    A = np.array([[1, 1, 0, 3], [0, 2, -1, 1], [0, 0, -1, 2], [0, 0, 0, -2]])
    b = np.array([5, 2, 1, -2]) #matriz coluna

    return A, b

def substituicao_inversa(A, b):
    n = len(b)
    x = np.zeros(n)    
    x[n-1] = b[n-1]/A[n-1][n-1]

    for i in range(n-2, -1, -1):
        soma = b[i]
        for j in range(i+1, n):
            soma -= A[i][j]*x[j]
            # print(A[i][j])
        x[i] = soma/A[i][i]

    print('X =', x)

def main():
    A, b = matrix()
    substituicao_inversa(A, b)
        
main()