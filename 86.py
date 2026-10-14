#ejercicio 86
pares = 0
impares = 0

print(" Lector de 10 Numeros (Pares e Impares) ")

for i in range(10):
  numero = int(input(f"Ingresa el numero: {i + 1}: "))

  
  if numero % 2 == 0:
    pares += 1
  else:
    impares += 1

print("RESULTADOS: ")
print("Total de números pares: ", pares)
print("Total de números impares: " , impares )
