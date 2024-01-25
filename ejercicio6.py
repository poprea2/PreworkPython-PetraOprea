'''BUCLES
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for. 
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while. 
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.'''


numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers: 
    print(number)
    
    
for number in range (1, 11):
    print(number)
    
    
z = 1
while z <= 20:
    if z % 2 == 0:
        print(z)
    z += 1
    

suma = 0
for numero in range (1, 101):
    suma += numero
    print(suma)
    
y = 1
suma = 0
while y <= 100:
    suma = suma + y
    y += 1
print("La suma de los numeros del 1 al 100 es:", suma)
    