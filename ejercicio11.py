"""Ejercicios nivel medio:
8. Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. 
Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. 
Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
9. Define una función que reciba un número y retorne su representación en binario.
10. Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).
11. Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
12. Escribe un programa que imprima los números del 1 al 50, 
pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de cinco imprima “Buzz”. 
Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.
13. Define una función que tome una lista y retorne la lista ordenada en orden ascendente.
14. Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.
15. Define una función que tome un número y calcule su serie de Fibonacci.
16. Define una función que tome una lista de números y retorne el número más grande de la lista."""




def numero_perfecto(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
            
    return suma == numero

num = int(input("Ingresa un numero: "))   
resultado = numero_perfecto(num)

if resultado:
    print(f"{num} es un numero perfecto.")    
else:
    print(f"{num} no es un número perfecto.")
    
    

def decimal_a_binario(numero):
    if numero < 0:
        return "Ingresa un numero positivo."
    else:
        return bin(numero)
num = int(input("Ingresa un numero: "))
binario = decimal_a_binario(num)
print(f"La representación binaria de {num} es: {binario}")



def interseccion_listas(lista1, lista2):
    return list(set(lista1) & set(lista2))
lista_1 = [6, 8, 10, 22, 34, 75, 80]
lista_2 = [7, 10, 22, 37, 85, 90, 75]
set_list = interseccion_listas(lista_1, lista_2)

print(f"Lista 1: {lista_1}")
print(f"Lista 2: {lista_2}")
print(f"interseccion: {set_list}")


def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]
texto = input("Ingresa una cadena para verificar si es un palíndromo:  ")
palabra = es_palindromo(texto)

if palabra:
    print(f"{texto} es un palíndromo")
else:
    print(f"{texto} no es un palíndromo")
    
    

for numero in range(1, 51):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
        
        

def ordenar_ascendente(lista):
    return sorted(lista)
mi_lista = [89, 45, 72, 12, 90, 7, 2, 33]     
lista = ordenar_ascendente(mi_lista)   

print(f"Lista original: {mi_lista}")
print(f"Lista en orden ascendente: {lista}")



def palabras_mas_largas_que_n(lista_palabras, n):
    return [palabra for palabra in lista_palabras if len(palabra) > n]
lista_palabras = ["armario", "programacion", "mesa", "palabra", "oso", "deliberacion"]
n = 5
palabras_largas = palabras_mas_largas_que_n(lista_palabras, n)

print(f"Lista de palabras: {lista_palabras}")
print(f"Palabras mas largas que {n}: {palabras_largas}")



def fibonacci_hasta_n(n):
    fibonacci = [0, 1]
    while fibonacci[-1] + fibonacci[-2] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci
numero = int(input("Ingresa un numero para calcular la serie de fibonacci: "))
serie_fibonacci = fibonacci_hasta_n(numero)

print(f"serie fibonacci hasta {numero}: {serie_fibonacci}")




def maximo(lista_numeros):
    maximo = lista_numeros[0]
    for numero in lista_numeros:
        if numero > maximo:
            maximo = numero
    return maximo
numeros = [11, 6, 29, 13, 32, 4]
maximo_numero = maximo(numeros)

print(f"Lista_numeros: {numeros}")
print(f"El numero mayor de la lista es: {maximo_numero}")








    


    




    
    