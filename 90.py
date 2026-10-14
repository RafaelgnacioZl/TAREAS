
while True:
    
    numero = int(input("¿De qué número deseas ver la tabla de multiplicar?: "))
    
    print(" Tabla de multiplicar del: ", numero)
    
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
   
    
  
    continuar = input("¿Deseas consultar otra tabla?: ").strip().lower()
    
    if continuar != 'si':
        print("\n¡Gracias por usar el programa! Hasta luego.")
        break
