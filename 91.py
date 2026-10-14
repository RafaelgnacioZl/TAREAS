
while True:
    print(" MENÚ CALCULADORA ")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Elige una opción del 1 al 5: ")
    
    match opcion:
        case "1":
            print(" Suma ")
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            
        case "2":
            print(" Resta ")
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            
        case "3":
            print("Multiplicación ")
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
            
        case "4":
            print(" División ")
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            if num2 != 0:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("No se puede dividir entre cero.")
                
        case "5":
            print(" Hasta luego.")
            break  
            
        case _:
            print(" Por favor, elige un número del 1 al 5.")
