def calcular_factorial(n):
    if n == 1:
        return 1
    return n * calcular_factorial(n-1)

num = int(input("Ingrese numero para calcular factorial: "))

factorial = calcular_factorial(num)

print(f"El factorial de {num} es {factorial}")
