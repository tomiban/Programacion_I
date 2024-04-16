def multi_Y_division(a, b):
    try:
        return (a*b, a/b)
    except ZeroDivisionError:
        print("Error: Divison por cero")
    
  
result = multi_Y_division(2,6)
if(result):
    print(f"Multiplicacion: {result[0]} - Division: {result[1]}")