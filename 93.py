def gestionar_notas():
    print(" SISTEMA DE REGISTRO DE NOTAS ")
    
    suma = 0
    contador = 0
    mayor = 0
    menor = 0
    respuesta = "s"
    
    while respuesta == "s" or respuesta == "S":
        nota = float(input("Ingrese la nota del estudiante: "))
       
        suma = suma + nota
        contador = contador + 1
        
     
        if contador == 1:
            mayor = nota
            menor = nota
        else:
            if nota > mayor:
                mayor = nota
            if nota < menor:
                menor = nota
                
        respuesta = input("¿Desea ingresar otra nota?: ")
        
    if contador > 0:
        promedio = suma / contador
        
        print(" + "=" * 34)
        print("            RESULTADOS            ")
       
        print("Total de estudiantes evaluados:", contador)
        print("Promedio general:", promedio)
        print("Nota más alta:", mayor)
        print("Nota más baja:", menor)
    else:
        print("No se registraron notas en el sistema.")


gestionar_notas()


