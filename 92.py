import math

def calcular_areas_geometricas():
    while True:
        
        print("  MENÚ DE FIGURAS GEOMÉTRICAS  ")
        print("1. Cuadrado")
        print("2. Rectángulo")
        print("3. Triángulo")
        print("4. Círculo")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        match opcion:
            case "1":
                print("Área del Cuadrado ")
                lado = float(input("Ingrese la medida del lado: "))
            
                if lado > 0:
                    area = lado ** 2
                    print(f"El área del cuadrado es: {area:.2f}")
                else:
                    print("Error: El lado debe ser mayor a cero.")
                    
            case "2":
                print(" Área del Rectángulo ")
                base = float(input("Ingrese la base: "))
                altura = float(input("Ingrese la altura: "))
                
         
 
                if base > 0 and altura > 0:
                    area = base * altura
                    print(f"El área del rectángulo es: {area:.2f}")
                else:
                    print("Error: Las dimensiones deben ser mayores a cero.")
                    
            case "3":
                print("Área del Triángulo ")
                base = float(input("Ingrese la base: "))
                altura = float(input("Ingrese la altura: "))
                
             
                if base > 0 and altura > 0:
                    area = (base * altura) / 2
                    print(f"El área del triángulo es: {area:.2f}")
                else:
                    print("Error: Las dimensiones deben ser mayores a cero.")
                    
            case "4":
                print(" Área del Círculo ")
                radio = float(input("Ingrese el radio: "))
                
               
                if radio > 0:
                    area = math.pi * (radio ** 2)
                    print(f"El área del círculo es: {area:.2f}")
                else:
                    print("Error: El radio debe ser mayor a cero.")
                    
            case "5":
                print("Hasta luego!")
                break  
                
            case _:
                print("Por favor, elija un número entre 1 y 5.")

if __name__ == "__main__":
    calcular_areas_geometricas()
