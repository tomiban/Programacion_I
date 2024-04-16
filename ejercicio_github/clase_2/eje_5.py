def convertir_farenheit(tem_celcius):
    return (tem_celcius * 1.8 )+ 32

def convertir_celcius(temp_faren):
    return (temp_faren - 32) * 0.555

def mostrar_temperatura(escala, temperatura):
    if(escala.lower() == "celcius"):
        return convertir_celcius(temperatura)
    elif (escala.lower() == "farenheit"):
        return convertir_farenheit(temperatura)
    
print(mostrar_temperatura("farenheit", 10))
print(mostrar_temperatura("celcius", 50))