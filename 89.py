
n = int(input("¿Cuántos números deseas ingresar?: "))

positivos = 0
negativos = 0
ceros = 0


for i in range(n):

    numero = float(input(f"Ingresa el número {i + 1}: "))
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

print(" Resultado Final: ")
print("Cantidad de números positivos: ", positivos)
print("Cantidad de números negativos: ", negativos )
print("Cantidad de ceros: ", ceros)
