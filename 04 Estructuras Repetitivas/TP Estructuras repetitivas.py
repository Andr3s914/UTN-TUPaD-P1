

# 1. Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
for numero in range(101):  
    print(numero)

# 2. Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.
numero = input("Introduce un número entero: ")  
cantidad_digitos = len(numero)  
print(f"El número tiene {cantidad_digitos} dígitos.")


# 3. Escribe un programa que sume todos los números enteros comprendidos entre dos valores

# Solicitar los valores al usuario
inicio = int(input("Introduce el primer número: "))  
fin = int(input("Introduce el segundo número: "))  

# Asegurar que inicio sea menor que fin
if inicio > fin:  
    inicio, fin = fin, inicio  

# Calcular la suma de los números entre ambos valores, excluyendo los extremos
suma = sum(range(inicio + 1, fin))  

print(f"La suma de los números entre {inicio} y {fin}, excluyendo los extremos, es: {suma}")



# 4. Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia.
suma_total = 0  

while True:  
    numero = int(input("Introduce un número entero (ingresa 0 para finalizar): "))  
    if numero == 0:  
        break  
    suma_total += numero  

print(f"La suma total de los números ingresados es: {suma_total}")



# 5. Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random  

numero_secreto = random.randint(0, 9)  
intentos = 0  

while True:  
    intento = int(input("Adivina el número (entre 0 y 9): "))  
    intentos += 1  

    if intento == numero_secreto:  
        print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")  
        break  
    else:  
        print("Intenta nuevamente.")  


# 6. Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
for numero in range(100, -1, -2):  
    print(numero)


# 7. Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
numero = int(input("Introduce un número entero positivo: "))  

if numero < 0:  
    print("Por favor, ingresa un número positivo.")  
else:  
    suma = sum(range(numero + 1))  
    print(f"La suma de los números entre 0 y {numero} es: {suma}")


# 8. Escribe un programa que permita al usuario ingresar 100 números enteros.

# Inicializar contadores
pares = impares = positivos = negativos = 0  

# Solicitar números al usuario
cantidad = 100  # Se puede cambiar fácilmente para pruebas
print(f"Ingrese {cantidad} números enteros:")

for _ in range(cantidad):  
    numero = int(input("Número: "))  

    if numero % 2 == 0:  
        pares += 1  
    else:  
        impares += 1  

    if numero > 0:  
        positivos += 1  
    elif numero < 0:  
        negativos += 1  

# Mostrar resultados
print(f"\nResultados:\nPares: {pares}\nImpares: {impares}\nPositivos: {positivos}\nNegativos: {negativos}")




# 9. Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.

# Inicializar la lista para almacenar los números
numeros = []  
cantidad = 100  # Puedes cambiar este valor para pruebas con menos números

print(f"Ingrese {cantidad} números enteros:")

for _ in range(cantidad):  
    numero = int(input("Número: "))  
    numeros.append(numero)  

# Calcular la media
media = sum(numeros) / cantidad  

print(f"\nLa media de los números ingresados es: {media}")




# 10. Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = input("Introduce un número entero: ")  
numero_invertido = numero[::-1]  
print(f"El número invertido es: {numero_invertido}")




