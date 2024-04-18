#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

valor = -2
if(valor < 0):
    print("El numero es MENOR a cero")
elif(valor > 0):
    print("El numero es MAYOR a cero")
else:
    print("El numero es IGUAL a cero")

# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:
variable_A = 2
variable_B = 4
if(type(variable_A) == type(variable_B)):
    print("Las variables son del mismo tipo de dato")
else:
    print("Las variables son de DIFERENTE tipo de dato")




# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
def obtener_numeros(num):
    pares = [] 
    impares = []   
    for i in range(num):
        if i % 2 == 0: 
            pares.append(i)
        elif i % 2 == 1:
            impares.append(i)    
    return pares, impares

num = 21
print(obtener_numeros(num))



# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for i in range(6):
    print("Rango de valor", i, "Elevado a la tercera potencia", i**3)
    


# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
n = 5
for i in range(n):
    print(++i)



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

numero = -2
while True:
    if numero > 0:
        print(numero)
        break
    else:
        print("El numero", numero,"no petenece al conjunto de numeros naturales")
        break

# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

txt = "Hola Mundo"
while True:
    for palabra in txt:
        if palabra == "o":
            print("Esta")
            continue
        else:
            print("No esta")
    break


# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:





# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def generar_primos(limite):
    primos = []
    for numero in range(2, limite + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

limite = 30
lista_primos = generar_primos(limite)
print(f"Los primeros números primos son: {lista_primos}")



# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:





# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:




# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:





# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:




# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:



