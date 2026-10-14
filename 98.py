def estadisticas_notas():
    print(" ESTADÍSTICAS DE 10 NOTAS ")
    
    aprobadas = 0
    reprobadas = 0
    suma = 0
    
   
    for i in range(1, 11):
        nota = float(input(f"Ingrese la nota del estudiante {i} (0 a 100): "))
        
        suma = suma + nota
      
        if nota >= 60:
            aprobadas = aprobadas + 1
        else:
            reprobadas = reprobadas + 1
            
 
    promedio = suma / 10
    
   
    print("\n" + "=" * 34)
    print("            ESTADÍSTICAS          ")
    print("=" * 34)
    print("Total de notas evaluadas: 10")
    print("Cantidad de notas aprobadas:", aprobadas)
    print("Cantidad de notas reprobadas:", reprobadas)
    print("Promedio general del grupo:", promedio)

estadisticas_notas()
