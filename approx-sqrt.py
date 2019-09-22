def sqrt(x):
    z = 1.0
    while abs(z*z-x) >= 0.01:
        z -= (z*z-x)/(2*z)

    return z
print(sqrt(8.0))