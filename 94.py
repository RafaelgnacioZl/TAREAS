def gestionar_edades():
    print("REGISTRO DE EDADES ")
    print("Nota: Ingrese 0 para finalizar el programa.")
    
    cant_mayores = 0
    cant_menores = 0
    
   
    edad = int(input("Ingrese la edad (o 0 para salir): "))
    
    
    while edad != 0:
        
        if edad >= 18:
            cant_mayores = cant_mayores + 1
        else:
            cant_menores = cant_menores + 1
            
        
        edad = int(input("Ingrese la edad (o 0 para salir): "))
        
   
    print("\n" + "=" * 34)
    print("            RESULTADOS            ")
    print("=" * 34)
    print("Cantidad de mayores de edad:", cant_mayores)
    print("Cantidad de menores de edad:", cant_menores)

gestionar_edades()
