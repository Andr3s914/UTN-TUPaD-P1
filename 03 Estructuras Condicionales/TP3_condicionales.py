#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# Solicitar la edad del usuario
edad = int(input("Por favor, ingresa tu edad: "))

# Verificar si el usuario es mayor de edad
if edad > 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")



#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

# Solicitar la nota del usuario
nota = float(input("Por favor, ingresa tu nota: "))

# Verificar si la nota es mayor o igual a 6
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

while True:
    # Solicitar un número al usuario
    numero = int(input("Por favor, ingrese un número par: "))

    # Verificar si el número es par
    if numero % 2 == 0:
        print("Ha ingresado un número par.")
        break  # Salir del bucle si el número es par
    else:
        print("Por favor, ingrese un número par.")


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:

# Solicitar la edad del usuario
edad = int(input("Por favor, ingrese su edad: "))

# Evaluar la categoría según la edad
if edad < 12:
    print("Niño/a: menor de 12 años.")
elif 12 <= edad < 18:
    print("Adolescente: mayor o igual que 12 años y menor que 18 años.")
elif 18 <= edad < 30:
    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
else:
    print("Adulto/a: mayor o igual que 30 años.")



#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

# Solicitar una contraseña al usuario
contraseña = input("Por favor, ingrese una contraseña: ")

# Verificar la longitud de la contraseña
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números

import random
from statistics import mode, median, mean

# Generar la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Determinar el tipo de sesgo
if media > mediana > moda:
    sesgo = "positivo (a la derecha)"
elif media < mediana < moda:
    sesgo = "negativo (a la izquierda)"
else:
    sesgo = "sin sesgo"

# Imprimir los resultados
print(f"Lista de números: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media:.2f}")
print(f"El conjunto tiene un sesgo {sesgo}.")


#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# Solicitar una frase o palabra al usuario
texto = input("Por favor, ingrese una frase o palabra: ")

# Verificar si el último carácter es una vocal
if texto[-1].lower() in 'aeiou':
    resultado = texto + "!"
else:
    resultado = texto

# Imprimir el resultado
print(resultado)


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:

# Solicitar el nombre del usuario
nombre = input("Por favor, ingrese su nombre: ")

# Solicitar la opción deseada
print("Seleccione una opción:")
print("1. Nombre en mayúsculas.")
print("2. Nombre en minúsculas.")
print("3. Nombre con la primera letra en mayúscula.")
opcion = int(input("Ingrese el número de la opción: "))

# Transformar el nombre según la opción seleccionada
if opcion == 1:
    resultado = nombre.upper()
elif opcion == 2:
    resultado = nombre.lower()
elif opcion == 3:
    resultado = nombre.title()
else:
    resultado = "Opción inválida. Por favor, intente nuevamente."

# Imprimir el resultado
print(resultado)


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:

# Solicitar la magnitud del terremoto al usuario
magnitud = float(input("Por favor, ingrese la magnitud del terremoto: "))

# Clasificar la magnitud según la escala de Richter
if magnitud < 3:
    clasificacion = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    clasificacion = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    clasificacion = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    clasificacion = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    clasificacion = "Muy fuerte (puede causar daños significativos)"
else:
    clasificacion = "Extremo (puede causar graves daños a gran escala)"

# Imprimir la clasificación
print(f"El terremoto tiene una clasificación de: {clasificacion}")


