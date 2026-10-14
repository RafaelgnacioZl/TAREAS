def clasificar_edades():
    print(" CLASIFICADOR DE EDADES ")
    
    n = int(input("¿Cuántas edades desea registrar? :"))
    
    ninos = 0
    adolescentes = 0
    adultos = 0
    adultos_mayores = 0
    
  
    for i in range(1, n + 1):
        edad = int(input(f"Ingrese la edad de la persona : "))
        
       
        if edad >= 0 and edad <= 12:
            ninos = ninos + 1
        elif edad >= 13 and edad <= 17:
            adolescentes = adolescentes + 1
        elif edad >= 18 and edad <= 59:
            adultos = adultos + 1
        elif edad >= 60:
            adultos_mayores = adultos_mayores + 1
        else:
            print("Edad no válida. Ingrese un valor mayor o igual a 0.")
            
    
    print("\n" + "=" * 34)
    print("            ESTADÍSTICAS          ")
    print("=" * 34)
    print("Total de personas evaluadas:", n)
    print("Niños (0 a 12 años):", ninos)
    print("Adolescentes (13 a 17 años):", adolescentes)
    print("Adultos (18 a 59 años):", adultos)
    print("Adultos mayores (60+ años):", adultos_mayores)

clasificar_edades()
