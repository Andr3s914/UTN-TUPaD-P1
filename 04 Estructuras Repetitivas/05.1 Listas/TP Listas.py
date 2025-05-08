
#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)


#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.

# Lista con cinco elementos que me gustan
cosas_que_me_gustan = ["Xbox", "Cine", "Música", "Comics", "tecnología"]

# Mostrar el penúltimo elemento usando índice negativo
print(cosas_que_me_gustan[-2])



#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla

# Crear una lista vacía
lista_vacia = []

# Agregar tres palabras con append
lista_vacia.append("Python")
lista_vacia.append("Aprendizaje")
lista_vacia.append("Creatividad")

# Imprimir la lista resultante
print(lista_vacia)



#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.

# Lista original
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazar el segundo y último valor
animales[1] = "loro"  # Segundo elemento (índice 1)
animales[-1] = "oso"  # Último elemento (índice -1)

# Imprimir la lista resultante
print(animales)



#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

#Define una lista llamada numeros con los valores [8, 15, 3, 22, 7].
#Elimina el valor máximo de la lista numeros usando el método remove(). El valor máximo se obtiene con max(numeros), que en este caso es 22.
#Imprime la lista después de haber eliminado el valor máximo.
#El resultado final seria [8, 15, 3, 7], ya que se elimina el número 22.


#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

# Crear la lista con números del 10 al 30, saltando de 5 en 5
numeros = list(range(10, 31, 5))

# Mostrar los dos primeros números
print(numeros[:2])


#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera

# Lista original
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazar los valores en los índices 1 y 2
autos[1] = "camioneta"
autos[2] = "deportivo"

# Imprimir la lista resultante
print(autos)


#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

# Crear lista vacía
dobles = []

# Agregar el doble de 5, 10 y 15
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# Imprimir la lista resultante
print(dobles)


#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes

# Lista inicial con productos comprados por diferentes clientes
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")

# d) Imprimir la lista resultante
print(compras)


#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos

# Crear la lista anidada con los elementos especificados
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

# Imprimir la lista resultante
print(lista_anidada)