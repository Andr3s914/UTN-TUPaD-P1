
#1 Crear una funcion llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”

# Definimos la funcion
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Llamamos a la funcion desde el programa principal
if __name__ == "__main__":
    imprimir_hola_mundo()



#2 Crear una funcion llamada saludar_usuario(nombre)

# Definimos la funcion que genra el saludo personalizado
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal
if __name__ == "__main__":
    nombre_usuario = input("Ingresa tu nombre: ")  # Solicitamos el nombre al usuario
    saludo = saludar_usuario(nombre_usuario)  # Llamamos a la funcion con el nombre ingresado
    print(saludo)  # Mostramos el saludo personalizado


#3 Crear una función llamada informacion_personal(nombre, apellido, edad, residencia)

# Definimos la funcion que muestra la informacion personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
if __name__ == "__main__":
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    residencia = input("Ingresa tu lugar de residencia: ")

    informacion_personal(nombre, apellido, edad, residencia)  # Llamamos a la funcion con los datos ingresados


#4 Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_ circulo(radio)

import math  # Importamos el módulo math para usar π

# Función para calcular el área del círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

# Función para calcular el perímetro del círculo
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
if __name__ == "__main__":
    radio = float(input("Ingresa el radio del círculo: "))  # Solicitamos el radio al usuario
    area = calcular_area_circulo(radio)  # Calculamos el área
    perimetro = calcular_perimetro_circulo(radio)  # Calculamos el perímetro

    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")


#5 Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes

# Definimos la funcion que convierte segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600  # 1 hora = 3600 segundos

# Programa principal
if __name__ == "__main__":
    segundos = int(input("Ingresa la cantidad de segundos: "))  # Solicitamos los segundos al usuario
    horas = segundos_a_horas(segundos)  # Convertimos los segundos a horas
    print(f"{segundos} segundos equivalen a {horas:.2f} horas.")  # Mostramos el resultado con dos decimales



#6 Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10

# Definimos la funcion que imprime la tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):  # Iteramos de 1 a 10
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
if __name__ == "__main__":
    numero = int(input("Ingresa un número: "))  # Solicitamos el número al usuario
    tabla_multiplicar(numero)  # Llamamos a la funcion


#7 Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros

# Definimos la funcion que realiza las operaciones basicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Indefinido (division por cero)"
    return (suma, resta, multiplicacion, division)

# Programa principal
if __name__ == "__main__":
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    resultados = operaciones_basicas(a, b)  # Llamamos a la funcion
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicacion: {resultados[2]}")
    print(f"Division: {resultados[3]}")


#8 Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal

# Definimos la funcion que calcula el indice de Masa Corporal (IMC)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
if __name__ == "__main__":
    peso = float(input("Ingresa tu peso en kg: "))  # Solicitamos el peso al usuario
    altura = float(input("Ingresa tu altura en metros: "))  # Solicitamos la altura al usuario

    imc = calcular_imc(peso, altura)  # Calculamos el IMC
    print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")  # Mostramos el resultado con dos decimales


#9 Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit

# Definimos la funcion que realiza la conversion
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal
if __name__ == "__main__":
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))  # Solicitamos la temperatura al usuario
    fahrenheit = celsius_a_fahrenheit(celsius)  # Convertimos a Fahrenheit
    print(f"{celsius:.2f}°C equivalen a {fahrenheit:.2f}°F")  # Mostramos el resultado con dos decimales


#10 Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.

# Definimos la funcion que calcula el promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
if __name__ == "__main__":
    a = float(input("Ingresa el primer numero: "))  # Solicitamos el primer número al usuario
    b = float(input("Ingresa el segundo numero: "))  # Solicitamos el segundo número
    c = float(input("Ingresa el tercer numero: "))  # Solicitamos el tercer numero

    promedio = calcular_promedio(a, b, c)  # Calculamos el promedio
    print(f"El promedio de {a}, {b} y {c} es: {promedio:.2f}")  # Mostramos el resultado con dos decimales

