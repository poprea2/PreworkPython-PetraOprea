"""   
27. Define una función que tome una lista y retorne la lista sin duplicados.
28. Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.
29. Define una función que reciba una lista de números y retorne el promedio de los números en la lista.
30. Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
31. Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.
32. Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.
33. Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.
34.  Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.
35.  Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False. """



def eliminar_duplicados(lista):
    return list(set(lista))
mi_lista = [6, 6, 7, 8, 9, 0, 0, 8, 13]
resultado = eliminar_duplicados(mi_lista)

print(f"Mi lista: {mi_lista}")
print(f"Lista sin duplicados: {resultado}")



def suma_cuadrados_pares(numero):
    suma = sum(x**2 for x in range(2, numero + 1, 2))
    return suma
mi_numero = int(input("Ingresa un número entero positivo:  "))
resultado = suma_cuadrados_pares(mi_numero)

print(f"Suma cuadrados pares hasta {mi_numero}: {resultado}")



def calcular_promedio(lista):
    suma = sum(lista)
    promedio = suma // len(lista)
    return promedio
numeros = [8, 9, 10, 12, 17, 19, 20]
resultado = calcular_promedio(numeros)

print(f"Lista números: {numeros}")
print(f"Promedio: {resultado}")



def cadena_mas_larga(lista_cadenas):
    mas_larga = max(lista_cadenas, key=len)
    return mas_larga
cadenas = ["localización", "deber", "programación", "lista", "película"]
resultado = cadena_mas_larga(cadenas)

print(f"Lista: {cadenas}")
print(f"Cadena más larga: {resultado}")



def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
primos = [x for x in range(15) if es_primo(x)]
print(f"Primeros primos: {primos}")



def invertir_palabras(cadena):
    palabras = cadena.split()
    palabras_invertidas = palabras[::-1]
    cadena_invertida = ' '.join(palabras_invertidas)
    return cadena_invertida
mi_cadena = "La curiosidad es una habilidad"
resultado = invertir_palabras(mi_cadena)

print(f"Mi cadena: {mi_cadena}")
print(f"Cadena con palabras invertidas: {resultado}")



def ultimo_elemento(lista_de_tuplas):
    return sorted(lista_de_tuplas, key=lambda tupla: tupla[-1])
tuplas = [(2, 6, 4), (23, 28, 30), (7, 9, 11), (15, 20, 17)]
lista_ordenada = ultimo_elemento(tuplas)

print(f"Lista de tuplas: {tuplas}")
print(f"Lista ordenada por último elemento: {lista_ordenada}")



def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    cantidad_vocales = sum(1 for letra in cadena if letra in vocales)
    return cantidad_vocales
mi_cadena = "Bienvenido al mundo digital"
resultado = contar_vocales(mi_cadena)

print(f"Cadena: {mi_cadena}")
print(f"Cantidad vocales: {resultado}")


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
mi_numero = int(input("Ingresa un numero: "))
resultado = es_primo(mi_numero)

print(resultado)



    


    
