def analizar_numeros():
    print("=== ANALIZADOR DE NÚMEROS ===")
    print("Nota: Ingrese 0 para finalizar el programa.\n")
    
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
   
    numero = int(input("Ingrese un número (o 0 para salir): "))
    
    while numero != 0:
        
        if numero > 0:
            positivos = positivos + 1
        elif numero < 0:
            negativos = negativos + 1
           )
        if numero % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
            

        numero = int(input("Ingrese un número (o 0 para salir): "))
       
    
    print("\n" + "=" * 34)
    print("            RESULTADOS            ")
    print("=" * 34)
    print("Cantidad de números pares:", pares)
    print("Cantidad de números impares:", impares)
    print("Cantidad de números positivos:", positivos)
    print("Cantidad de números negativos:", negativos)

analizar_numeros()
