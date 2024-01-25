""" 
17. Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
18. Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
19. Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.
20. Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.
21. Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
22. Define una función que reciba una lista de números y retorne la suma acumulada de los números.
23. Define una función que encuentre el elemento más común en una lista. 
24. Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.
25. Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.
26. Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas."""




def suma_digitos_al_cubo(numero):
    suma_cubos = 0
    
    for digito in str(abs(numero)):
        suma_cubos += int(digito) ** 3
    return suma_cubos
numero = int(input("Ingresa un numero: "))
resultado = suma_digitos_al_cubo(numero)

print(f"El número: {numero}")
print(f"La suma de los digitos al cubo es: {resultado}")


def segundo_mas_grande(lista_numeros):
    if len(lista_numeros) < 2:
        return None
    lista_ordenada = sorted(set(lista_numeros), reverse=True)
    return lista_ordenada[1]
numeros = [8, 15, 17, 22, 9, 2]
segundo_mayor = segundo_mas_grande(numeros)
print(f"Mi lista: {numeros}")
print(f"El segundo número más grande es: {segundo_mayor}")


def valores_en_comun(lista1, lista2):
    return bool(set(lista1) & set(lista2))
lista_a = [11, 12, 13, 15, 16, 18]
lista_b = [14, 17, 19, 22, 25, 27]
resultado = valores_en_comun(lista_a, lista_b)
print(f"Listas: {lista_a, lista_b}")
print(f"Hay valores en común: {resultado}")


def lista_inversa(lista):
    return lista [::-1]
mi_lista = [5, 8, 12, 16, 18, 22]
resultado = lista_inversa(mi_lista)
print(f"Lista original: {mi_lista}")
print(f"Lista en orden inverso: {resultado}")


def contar_digitos_letras(cadena):
    contador_digitos = 0
    contador_letras = 0
    for caracter in cadena:
        if caracter.isdigit():
            contador_digitos += 1
        elif caracter.isalpha():
            contador_letras += 1
    return contador_digitos, contador_letras
mi_cadena = "Python345Cadena678"
digitos, letras = contar_digitos_letras(mi_cadena)

print(f"Cadena: {mi_cadena}")
print(f"Número de digitos: {digitos}")
print(f"Número de letras: {letras}")


def suma_acumulada(lista):
    suma = 0
    suma_acumulada_resultado = []
    for numero in lista:
        suma += numero
        suma_acumulada_resultado.append(suma)
    return suma_acumulada_resultado
numeros = [5, 8, 12, 18, 22, 27]
resultado = suma_acumulada(numeros)

print(f"Lista de números: {numeros}")
print(f"Suma acumulada: {resultado}")


def elemento_mas_comun(lista):
    if not lista:
        return None
    return max(set(lista), key=lista.count)

mi_lista = [2, 4, 2, 6, 4, 2, 8, 10, 2, 6, 4]
resultado = elemento_mas_comun(mi_lista)

print(f"Lista original: {mi_lista}")
print(f"El elemento más común es: {resultado}")


        
def tabla_multiplicar(numero):
    tabla = {}
    for i in range(1, 11):
        tabla[i] = numero * i
    return tabla
num = int(input("Ingresa un número para obtener la tabla de multiplicar: "))
resultado = tabla_multiplicar(num)

print(f"Tabla de multiplicar del {num} del 1 al 10:")
for key, value in resultado.items():
    print(f"{num} x {key} = {value}") 



def contar_caracteres(cadena):
    diccionario_apariciones = {}
    
    for caracter in cadena:
        if caracter in diccionario_apariciones:
            diccionario_apariciones[caracter] += 1
        else:
            diccionario_apariciones[caracter] = 1
    return diccionario_apariciones
mi_cadena = "Una maravillosa herramienta"
resultado = contar_caracteres(mi_cadena)

print(f"Cadena: {mi_cadena}")
print(f"Apariciones de cada carácter:")
for caracter, apariciones in resultado.items():
    print(f"'{caracter}' : {apariciones}")
    
    

def elementos_no_comunes(lista1, lista2):
    conjunto1 = set(lista1)   
    conjunto2 = set(lista2)
    elementos_no_comunes = list(conjunto1.symmetric_difference(conjunto2))
    return elementos_no_comunes

lista_a = [8, 9, 10, 11, 13]
lista_b = [8, 9, 22, 17, 30]
resultado = elementos_no_comunes(lista_a, lista_b)

print(f"Lista 1: {lista_a}")
print(f"Lista 2: {lista_b}")
print(f"Elementos no comunes: {resultado}")
            
    
