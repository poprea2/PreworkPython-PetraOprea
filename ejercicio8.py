"""1. Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar” según corresponda.
2. Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado.
3. Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado total de dígitos.
4. Dada una lista de números, crea una función que devuelva el número máximo de la lista.
5. Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.
6. Dados dos números, crea una función para encontrar el mínimo común múltiplo (MCM) de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM.
"""

def es_par(numero):
    return numero % 2 == 0
num = int(input("Ingresa un numero: "))
if es_par(num):
    print("El numero es par.")
else:
    print("El numero es impar.")
    
    
def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
        return resultado
num = int(input("Ingresa un numero: "))
print("El factorial de", num, "es:", factorial(num))


def contar_digitos(numero):
    return len(str(numero))
num = int(input("Ingresa un numero: "))
print("La cantidad de digitos es:", contar_digitos(num))


def encontrar_maximo(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
            return maximo
numeros = [56, 12, 8, 92, 30]
print("El numero maximo es:", encontrar_maximo(numeros))


def sumar_digitos(numero):
    suma = 0
    while numero > 0: 
        suma += numero % 10
        numero //= 10
        return suma
num = int(input("Ingresa un numero: "))
print("La suma de los digitos es:", sumar_digitos(num))


def mcm(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        maximo = max(a, b)
        while True:
            if maximo % a == 0 and maximo % b == 0:
                return maximo
            maximo += 1
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
print("El mcm es:", mcm(num1, num2))






        
        



         
    
