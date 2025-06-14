#1 Crea una función recursiva que calcule el factorial de un número. Luego...

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Solicitar al usuario un numero
num = int(input("Introduce un número entero: "))

# Mostrar el factorial de cada numero entre 1 y num
for i in range(1, num + 1):
    print(f"Factorial de {i}: {factorial(i)}")


#2 Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada...

def fibonacci(n):
    if n <= 0:
        return "La posicion debe ser un numero entero positivo."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Solicitar al usuario una posicion
posicion = int(input("Introduce la posicion hasta la que deseas ver la serie de Fibonacci: "))

# Mostrar la serie completa
serie = [fibonacci(i) for i in range(1, posicion + 1)]
print(f"Serie de Fibonacci hasta la posicion {posicion}: {serie}")


#3 Crea una función recursiva que calcule la potencia de un número base elevado a un exponente...

def potencia(base, exponente):
    if exponente == 0:  # Caso base: cualquier numero elevado a 0 es 1
        return 1
    return base * potencia(base, exponente - 1)

# Probemos la funcion con un algoritmo general
if __name__ == "__main__":
    base = int(input("Ingresa la base: "))
    exponente = int(input("Ingresa el exponente: "))
    resultado = potencia(base, exponente)
    print(f"{base}^{exponente} = {resultado}")


#4 Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto

def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

# Probemos la funcion
numero = 10
binario = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {binario}")


#5 Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tilde...

def es_palindromo(palabra):
    if len(palabra) <= 1:  # Caso base: una palabra vacia o de un solo caracter es un palindromo
        return True
    if palabra[0] != palabra[-1]:  # Si los extremos no coinciden, no es un palindromo
        return False
    return es_palindromo(palabra[1:-1])  # Llamada recursiva con la palabra sin los extremos

# Pruebas
palabras = ["reconocer", "radar", "python", "neuquen"]
for palabra in palabras:
    print(f"{palabra}: {es_palindromo(palabra)}")


#6 Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos...

def suma_digitos(n):
    if n == 0:  # Caso base: si n es 0, la suma de los digitos es 0
        return 0
    return (n % 10) + suma_digitos(n // 10)  # Extraemo el ultimo digito y sumamos recursivamente el resto

# Pruebas
numeros = [1234, 9, 305]
for numero in numeros:
    print(f"suma_digitos({numero}) → {suma_digitos(numero)}")


#7 Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos...

def contar_bloques(n):
    if n == 1:  # Caso base: cuando solo hay un bloque, el total es 1
        return 1
    return n + contar_bloques(n - 1)  # Se suma el nivel actual y se llama recursivamente con el siguiente nivel

# Pruebas
niveles = [1, 2, 4, 5]
for nivel in niveles:
    print(f"contar_bloques({nivel}) → {contar_bloques(nivel)}")

#8 Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo...

def contar_digito(numero, digito):
    if numero == 0:  # Caso base: si el numero es 0, no hay mas digitos que contar
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)  # Compara el ultimo digito y sigue con el resto

# Pruebas
ejemplos = [(12233421, 2), (5555, 5), (123456, 7)]
for numero, digito in ejemplos:
    print(f"contar_digito({numero}, {digito}) → {contar_digito(numero, digito)}")