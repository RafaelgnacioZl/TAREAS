print("El Mayor y Menor de 10 Números ")

mayor = 0
menor = 0

for i in range(10):
  
  numero = int(input(f"Ingresa el número {i + 1}: "))

  if i == 0:
    mayor = numero
    menor = numero
  else:
   
    if numero > mayor:
      mayor = numero

    if numero < menor:
      menor = numero

print("Resultados: ")
print("El número mayor es: ", mayor)
print("El número menor es: ", menor)
