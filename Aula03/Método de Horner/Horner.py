import numpy as np

def horner(x0, a):
    n = len(a)
    y = a[-1]
    z = y

    for j in range(n-2, 0, -1):
        y = x0 * y + a[j]
        z = x0 * z + y
    y = x0*y + a[0]

    return y,z 

def main():
    a = (-4, 3, -3, 0, 2) #p(x) 2x⁴-3x²+3x-4

    x0 = -2
    tol = 1.0e-6
    it = 1
    itmax = 100

    y, z = horner(x0, a)
    while (abs(y) > tol and it < itmax):
        x = x0 - y/z
        x0 = x
        y, z = horner(x0, a)
        print(it, x, abs(y))
        it += 1

main()