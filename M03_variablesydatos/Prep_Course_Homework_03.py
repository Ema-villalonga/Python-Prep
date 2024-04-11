#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

edad = 27
print(edad)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

MI_CONSTANTE = 8.5
print(type(MI_CONSTANTE))



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
print(type(edad))




# 4) Crear una variable que contenga tu nombre

# In[2]:

nombre = "Emanuel"
print(nombre)


# 5) Crear una variable que contenga un número complejo

# In[3]:

numero_complejo = 2+3j




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

print(type(numero_complejo))



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

booleano_uno = 'True'
booleano_dos = True



# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print(type(booleano_uno))
print(type(booleano_dos))



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

suma = 5 + 2.2
print(suma)


# 11) Realizar una operación de suma de números complejos

# In[2]:

suma_complejo = 1+2j + 2+2j
print(suma_complejo)




# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

suma_real_complejo = 2.5 + 2+1j
print(suma_real_complejo)



# 13) Realizar una operación de multiplicación

# In[5]:

multiplicacion = 5 * 5
print(multiplicacion)




# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

elevar_dos = 2**8
print(elevar_dos)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

x = 27
y = 4
division = x / y
print(division)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
x = 27
y = 4
division_entera = x // y
print(division_entera)




# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
x = 27
y = 4

division_resto = x % y 
print(division_resto)




# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
x = 27
y = 4
resultado_dieciseis = x // y 
resultado_final = resultado_dieciseis * 4 + 3
print(resultado_final)



# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
a = 2
b = 3
print(a + b)


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

num_uno = "2"
num_dos = 2
print(num_uno == num_dos)
print(type(num_uno)) # string
print(type(num_dos)) # int


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

print(num_uno != num_dos)



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

#a = float('3,8') por que tiene una coma

a = float('3.8')
print(a)


# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

valor_tres = 3
valor_tres-=1
print(valor_tres)




# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

print(1<<2)

# multiplica una vez el dos
# El sistema de numeración binario solo utiliza dos digitos '0' y '1'

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:


#c = 2 + '2'
c = 2 + int('2')
print(c)

# por que no concatena cadena con entero, ya que necesita del metodo casting
# si los dos operandos son del mismo tipo de dato realiza la suma



# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

dos_entero = 2
dos_cadena = int('2')
print(dos_entero + dos_cadena)

# %%
