aprobados_con_nueve = 0
cant_aprobados = int(input("Ingresar la cantidad de estudiantes que aprobar el examen de fisica: "))

if(cant_aprobados == 0):
    print("Nadie Aprobó")
else:
    for i in range(cant_aprobados):
        nota = int(input(f"Ingrese la nota del alumno {i+1}: "))
        if(nota >= 9):
            aprobados_con_nueve += 1

    porcentaje = (aprobados_con_nueve * 100) / cant_aprobados 
    
    print(f"El porcentaje de alumnos que sacaron 9 o más es: {porcentaje}")
    
 



