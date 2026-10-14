def menu_bancario():
    print(" SISTEMA BANCARIO")
 
    saldo = 1000.00
    

    while True:
        print(" MENÚ PRINCIPAL ")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1 - 4): ").strip()
        
        match opcion:
            case "1":
                print(f"Su saldo actual es: ${saldo:.2f}")
                
            case "2":
                deposito = float(input("\nIngrese la cantidad a depositar: "))
                if deposito > 0:
                    saldo = saldo + deposito
                    print(f"¡Depósito exitoso! Su nuevo saldo es: ${saldo
