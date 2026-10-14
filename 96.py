def gestionar_compras():
    print("=== SISTEMA DE COMPRAS ===")
    
   
    total = 0
    
 
 
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar producto y precio")
        print("2. Finalizar")
        
        opcion = input("Seleccione una opción (1 o 2): ").strip()
       
        match opcion:
            case "1":
                producto = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                
                total = total + precio
                print(f"¡'{producto}' agregado con éxito!")
                
            case "2":
                print("\nSaliendo del sistema de registro...")
                break 
                
            case _:
                print(" Opción no válida. Por favor, elija 1 o 2.")
                
    print("\n" + "=" * 34)
    print("            RESULTADOS            ")
    print("=" * 34)
    print("Total acumulado a pagar:", total)
gestionar_compras()
