""" comision_1 = []
comision_2 = []
comision_3 = []
comision_4 = []
comision_5 = []

while True:
    
    entrada = input("Ingrese su nota final y numero de comision separado por un '-' / FIN para terminar")
    if(entrada == "FIN"):
        break;
    datos = entrada.split("-")
    nota = int(datos[0].strip())
    comision = int(datos[1].strip())
    
    if(comision == 1):
        comision_1.append(nota)
    elif(comision == 2):
        comision_2.append(nota)
    elif(comision == 3):
        comision_3.append(nota)
    elif(comision == 4):
        comision_4.append(nota)
    elif(comision == 5):
        comision_5.append(nota)
        
print(f"El promedio de la comision 1 es {sum(comision_1) / len(comision_1)}")
print(f"El promedio de la comision 2 es {sum(comision_2) / len(comision_2)}")
print(f"El promedio de la comision 3 es {sum(comision_3) / len(comision_3)}")
print(f"El promedio de la comision 4 es {sum(comision_4) / len(comision_4)}")
print(f"El promedio de la comision 5 es {sum(comision_5) / len(comision_5)}")
 """
 
comisiones = {}

while True:
    entrada = input("Ingrese su nota final y numero de comision separado por un '-' / FIN para terminar: ")
    
    if entrada == "FIN":
        break
    
    datos = entrada.split("-")
    nota = int(datos[0].strip())
    comision = int(datos[1].strip())
    
    if comision not in comisiones:
        comisiones[comision] = []
    
    comisiones[comision].append(nota)

for comision, notas in comisiones.items():
    if notas:
        promedio = sum(notas) / len(notas)
        print(f"El promedio de la comisión {comision} es {promedio}")
    