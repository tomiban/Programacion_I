alumnos = []

while True:
    entrada = input("Ingrese nombre completo y edad separados por coma (o 'FIN' para terminar): ")

    if entrada.upper() == "FIN":
        break

    datos = entrada.split(",")
    
    nombre = datos[0].strip()
    edad = int(datos[1].strip())
    
    alumno = {"nombre": nombre, "edad": edad}
    alumnos.append(alumno)

if not alumnos:
    print("No se ingresaron alumnos")
else:
    dos_alumnos_mayores = []
    mayor1 = {"nombre": "", "edad": 0}
    mayor2 = {"nombre": "", "edad": 0}
     
    for alumno in alumnos:
        if alumno["edad"] > mayor1["edad"]:
            mayor2 = mayor1.copy() # paso el diccionario del 1 al 2
            mayor1 = alumno.copy() # el 1 pasa a ser el alumno iterado
        elif alumno["edad"] > mayor2["edad"]:
            mayor2 = alumno.copy() #sino paso como mayor2 al alumno iterado
        
    dos_alumnos_mayores.append(mayor1)
    dos_alumnos_mayores.append(mayor2)
    
    print("Los dos alumnos con las edades más altas son:")
    for alumno in dos_alumnos_mayores:
        print(f"Nombre: {alumno['nombre']}, Edad: {alumno['edad']}")         
    