num_mayor = None

while True:
    num = input("Ingresar numero / FIN para terminar: ")
    if num.upper() == "FIN":
        break
    num = int(num)
    if num_mayor is None or num > num_mayor:
        num_mayor = num

if num_mayor is not None:
    print(f"El numero mas alto ingresado es: {num_mayor}")