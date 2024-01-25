'''Dado un número, imprime si es positivo o negativo'''
'''Dado un número, imprime si es par o impar'''
'''Dado tres números, encuentra y muestra el mayor de ellos'''


a = 13
if a > 0: 
    print("a es positivo")
    
elif a < 0:
    print("a es negativo")
    

b = 10
if b % 2 == 0:
     print ("b es impar")
     
else:
    print ("b es par")
    
n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
n3 = float(input("Ingresa el tercer número: "))

if n2 < n1 > n3:
    print("El numero mayor es el primero. Numero:",n1)
    
elif n1 < n2 > n3:
    print("El numero mayor es el segundo. Numero:",n2) 
    
elif n1 < n3 > n2:
    print("El numero mayor es el tercero. Numero:",n3)
    
else: 
    print("Todos los numeros son igules")
    
    
    

    
    


    
    
    