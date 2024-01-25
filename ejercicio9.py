"""1. Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo.
2. Crea una función que, dado un número, verifique si un número es positivo, negativo o cero.
3. Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.
4. Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto.
5. Crea una función que, dado un número, verifique si un número es primo.
6. Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números."""



def calcular_area_triangulo(base, altura):
    return (base * altura) / 2
base = float(input("Ingresa la base del triangulo: "))
altura = float(input("Ingresa la altura del triangulo: "))
print("El area del triangulo es:", calcular_area_triangulo(base, altura))


def verificar_signo(num):
    if num > 0:
        return "positivo"
    elif num < 0:
        return "negativo"
    else:
        return "cero"
num = float(input("Ingresa un numero: "))
print("El numero es:", verificar_signo(num))


def contar_letras(palabra):
    contador = 0
    for letra in palabra:
        if letra.isalpha(): 
           contador += 1
    return contador            
palabra = input("Ingresa una palabra: ")
print("La cantidad de letras es:", contar_letras(palabra))


def valor_absoluto(lista):
    for i in range(len(lista)):
        lista[i] = abs(lista[i])
    return lista
numeros = [5, -12, 3, -8, 9]
print("Lista con valores absolutos:", valor_absoluto(numeros))


def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
num = int(input("Ingresa un numero: "))
if es_primo(num):
    print("Es un numero primo.")
else:
    print("No es un numero primo.")
    
    
def mcd(a, b):
    while b: 
        a, b = b, a % b
    return a
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
print("El MCD es:", mcd(num1, num2))
        







            