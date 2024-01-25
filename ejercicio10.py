"""Ejercicios nivel medio:
1. Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci. 
2. Define una función que tome un número y retorne una lista de sus divisores. 
3. Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original. 
4. Define una función que tome un número y retorne la suma de sus dígitos.
5. Define una función que tome una cadena y cuente el número de vocales en la cadena. 
6. Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.
7. Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena."""



def fibonacci(n):
    fib_serie = []
    
    if n <= 0:
        print("Ingresa un numero positivo para n.")
        return
    elif n == 1:
        fib_serie = [0]
    elif n == 2:
        fib_serie = [0, 1]
    else:
        fib_serie = [0, 1]
        for i in range(2, n):
            fib_serie.append(fib_serie[-1] + fib_serie[-2])
    return fib_serie

n = int(input("Ingresa la cantidad de números de Fibonacci a imprimir: "))
resultado = fibonacci(n)
print(f"los primeros {n} numeros de la serie fibonacci son: {resultado}")



def lista_divisores(numero):
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    
    return divisores

print(lista_divisores(5))
print(lista_divisores(17))
print(lista_divisores(10))



def elementos_unicos(lista):
    return list(set(lista))

numeros = [3, 4, 4, 12, 10, 12, 24, 22, 22, 0, 0, 32]
resultado = elementos_unicos(numeros)

print(numeros)
print(resultado)

def elementos_unicos(lista):
    elementos_unicos = []
    for elemento in lista:
        if elemento not in elementos_unicos:
            elementos_unicos.append(elemento)
    return elementos_unicos

numeros = [3, 4, 4, 12, 10, 12, 24, 22, 22, 0, 0, 32]
resultado = elementos_unicos(numeros)

print(numeros)
print(resultado)




def suma_digitos(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma

mi_numero = 3897
suma = suma_digitos(mi_numero)

print(f"El numero: {mi_numero}")
print(f"La suma de los digitos es: {suma}")



def contar_vocales(cadena):
    cadena = cadena.lower()
    vocales = "aeiou"
    contador_vocales = 0
    
    for caracter in cadena:
        if caracter in vocales:
            contador_vocales += 1
    return contador_vocales

cadena_texto = "Hoy es miercoles"
resultado = contar_vocales(cadena_texto)

print(f"La cadena: {cadena_texto}")
print(f"El número de vocales es: {resultado}")



def primeros_n_elementos(lista, n):
    return lista[:n]
num_lista = [8, 14, 22, 28, 33, 96, 145, 232]
n = 6
resultado = primeros_n_elementos(num_lista, n)

print(f"Mi lista: {num_lista}")
print(f"Primeros {n} elementos: {resultado}")



  
def contar_mayus_minus(cadena):  
    contador_mayusculas = 0
    contador_minusculas = 0
    
    for c in cadena:
        if c.isupper():
            contador_mayusculas += 1
        elif c.islower():
            contador_minusculas += 1
            
    return contador_mayusculas, contador_minusculas

frase = "I was born in May"
print(f"La cadena es: {frase}")
print(contar_mayus_minus(frase))

        

    




    