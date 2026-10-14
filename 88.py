print("Suma y Promedio ")

n = int(input("¿Cuantos numeros ingresaras?  "))

suma = 0

for i in range(n):
  
  numero = float(input(f"Ingresa el número {i + 1}: "))

  suma += numero


if n > 0:
  promedio = suma / n

  print(" Resultados Finales ")
  print("La suma total es: ", suma )
  print("El promedio es: ", promedio)
else:
  print("La cantidad de números debe ser mayor a 0.")
