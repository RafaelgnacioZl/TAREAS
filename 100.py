def menu_matematico():
    
    while True:
        print("\n" + "=" * 36)
        print("     MENÚ DE OPERACIONES MATEMÁTICAS    ")
        print("=" * 36)
        print("1. Calcular Factorial")
        print("2. Mostrar Tabla de Multiplicar")
        print("3. Verificar Paridad (Par o Impar)")
        print("4. Calcular el Cuadrado de un Número")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        

        match opcion:
            case "1":
                print("CÁLCULO DE FACTORIAL ")
                num = int(input("Ingrese un número entero no negativo: "))
                
               
                if num < 0:
                    print("Error: El factorial no está definido para números negativos.")
                else:
                    factorial = 1
                    for i in range(1, num + 1):
                        factorial = factorial * i
                    print(f"El factorial de {num} es: {factorial}")
                    
            case "2":
                print("TABLA DE MULTIPLICAR ")
                num = int(input("Ingrese un número para ver su tabla: "))
                
                print(f"Tabla del {num}:")
                for i in range(1, 11):
                    resultado = num * i
                    print(f"{num} x {i} = {resultado}")
                    
            case "3":
                print("VERIFICAR PARIDAD ")
                num = int(input("Ingrese un número entero: "))
                
                
                if num % 2 == 0:
                    print(f"El número {num} es PAR.")
                else:
                    print(f"El número {num} es IMPAR.")
                    
            case "4":
                print(" CALCULAR CUADRADO ")
                num = float(input("Ingrese un número: "))
                cuadrado = num ** 2
                print(f"El cuadrado de {num} es: {cuadrado}")
                
            case "5":
                print(" ¡Hasta pronto!")
                break 
                
            case _:
                print("Por favor, seleccione una opción entre 1 y 5.")

menu_matematico()
