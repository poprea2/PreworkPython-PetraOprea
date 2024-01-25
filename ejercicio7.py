'''Funciones 
1. Ejercicio: Define una función que tome dos números y retorne su suma. 
2. Ejercicio: Define una función que tome un número y retorne su factorial. 
3. Ejercicio: Define una función que tome un número y determine si es primo. 
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos. 
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa. '''


def suma_numeros(n1, n2):
    suma = n1 + n2
    return suma

total = suma_numeros(18, 4)
print(total)

total = suma_numeros(4.2, 9)
print(total)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
resultado = factorial(number)
print(resultado)

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = 44
if es_primo:
    print("Es primo")
else:
    print("No es primo")
    

def suma_lista(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

numeros = [7, 62, 57, 88, 96, 125]
print(suma_lista(numeros))


def cadena_reversa(cadena):
    return cadena[::-1]

texto = "Hoy hace frio."
texto_invertido = cadena_reversa(texto)
print("Texto original:", texto)
print("Texto invertido:", texto_invertido)

texto = "Business Development"
texto_invertido = cadena_reversa(texto)
print("Texto original:", texto)
print("Texto invertido:", texto_invertido)



 
 
    
    

