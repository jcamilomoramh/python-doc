# comentario 

""" comentario de diferentes lineas """


from ast import Str
from contextlib import nullcontext
from termios import VT1


print("hola mundo")
#variable
i = 1
texto = "repaso de python"
nombre = " camilo"
numero = 200

#concadenacion de string y entero, con str se transforma el enero a un string   
print(texto + str(numero))


#Entrada  y salida 
sitioweb = input("cual es tu paguna web ")


#condiciones 
numeroString = str(1) # otra manera es poniendo comillas dobles en el numerp: "1"
StringEntero = int("242853293")


#funciones
def mostrarAltura(numeroString, sitioweb):
      resultado = ""

      if sitioweb ==  numeroString:
          print("por favor ingrese un texto")
          resultado ="gracias por ayudar"
      else:
           print(sitioweb)
           resultado = "fin"
      return resultado     
    

mostrarAltura(numeroString, sitioweb)
mostrarAltura(numeroString, sitioweb)
#se puede repetir el codigo llamando la funcion varias veces
print(mostrarAltura(numeroString, sitioweb))

#listas
personas= ["saul", "andres", "pepe"]
animales = ["perro", "gato", "elefante" ]
print(personas[0])
#convierte en listado el array
for v in personas:
    print(v)
#enlistar y enumerar array


for b in enumerate(personas):
    print(b)
#recorrrer un array al contrario    
for h in reversed(personas):
    print(h)
#enlistar dos arrays
for a,p in zip(animales,personas):
    print(a,p)
#tomar un elemento del array y separar caracteres


for b in enumerate(personas[1]):
    print(b)

#rango en orden y alcontrio
for r in range(len(personas)):
    print(r)    

for rangeR in range(len(personas)-0): 
     print(rangeR)   
    
    
#operadores logicos 

#Operadores aritméticos
"""
+	Realiza Adición entre los operandos	12 + 3 = 15
-	Realiza Substracción entre los operandos	12 - 3 = 9
*	Realiza Multiplicación entre los operandos	12 * 3 = 36
/	Realiza División entre los operandos	12 / 3 = 4
%	Realiza un módulo entre los operandos	16 % 3 = 1
**	Realiza la potencia de los operandos	12 ** 3 = 1728
//	Realiza la división con resultado de número entero	18 // 5 = 3"""
#Operadoes Relacionales

"""
>	Devuelve True si el operador de la izquierda es mayor que el operador de la derecha	12 > 3 devuelve True
<	Devuelve True si el operador de la derecha es mayor que el operador de la izquierda	12 < 3 devuelve False
==	Devuelve True si ambos operandos son iguales	12 == 3 devuelve False
>=	Devuelve True si el operador de la izquierda es mayor o igual que el operador de la derecha	12 >= 3 devuelve True
<=	Devuelve True si el operador de la derecha es mayor o igual que el operador de la izquierda	12 <= 3 devuelve False
!=	Devuelve True si ambos operandos no son iguales	12 != 3 devuelve True"""
#operador Bit a Bit

"""&	Realiza bit a bit la operación AND en los operandos	a & b = 2 (Binario: 10 & 11 = 10)
|	Realiza bit a bit la operación OR en los operandos	a | b = 3 (Binario: 10 | 11 = 11)
^	Realiza bit a bit la operación XOR en los operandos	a ^ b = 1 (Binario: 10 ^ 11 = 01)
~	Realiza bit a bit la operación NOT bit a bit. Invierte cada bit en el operando	~a = -3 (Binario: ~(00000010) = (11111101))
>>	Realiza un desplazamiento a la derecha bit a bit. Desplaza los bits del operador de la izquierda a la derecha tantos bits como indica el operador de la derecha	a >> b = 0 (Binario: 00000010 >> 00000011 = 0)
<<	Realiza un desplazamiento a la izquierda bit a bit. Desplaza los bits del operando de la izquierda a la izquierda tantos bits como especifique el operador de la derecha	a << b = 16 (Binario: 00000010 << 00000011 = 00001000)"""
#operdor Operadores de Asignación

"""=	a = 5. El valor 5 es asignado a la variable a
+=	a += 5 es equivalente a a = a + 5
-=	a -= 5 es equivalente a a = a - 5
*=	a *= 3 es equivalente a a = a * 3
/=	a /= 3 es equivalente a a = a / 3
%=	a %= 3 es equivalente a a = a % 3
**=	a **= 3 es equivalente a a = a ** 3
//=	a //= 3 es equivalente a a = a // 3
&=	a &= 3 es equivalente a a = a & 3
|=	a |= 3 es equivalente a a = a | 3
^=	a ^= 3 es equivalente a a = a ^ 3
>>=	a >>= 3 es equivalente a a = a >> 3
<<=	a <<= 3 es equivalente a a = a << 3"""

#Operadores Lógicos
"""and	Devuelve True si ambos operandos son True	a and b
or	Devuelve True si alguno de los operandos es True	a or b
not	Devuelve True si alguno de los operandos False	not a"""

#Operadores de Pertenencia
"""in y not in son operadores de pertenencia.

in devuelve True si el valor especificado se encuentra en la secuencia. En caso contrario devuelve False.

not in devuelve True si el valor especificado no se encuentra en la secuencia. En caso contrario devuelve False."""


a = [1,2,3,4,5]
  
#Esta 3 en la lista a?
print (3 in a) # Muestra True 
  
#No está 12 en la lista a?
print (12 not in a) # Muestra True
  
str = "Hello World"
  
#Contiene World el string str?
print ("World" in str) # Muestra True
  
#Contiene world el string str? (nota: distingue mayúsculas y minúsculas)
print ("world" in str) # Muestra False  

print ("code" not in str) # Muestra True

#Operadores de Identidad
"""Un operador de identidad se emplea para comprobar si dos variables emplean la misma ubicación en memoria.

is y is not son operadores de identidad.

is devuelve True si los operandos se refieren al mismo objeto. En caso contrario devuelve False.

is not devuelve True si los operandos no se refieren al mismo objeto. En caso contrario devuelve False.

Ten en cuenta que dos valores, cuando son iguales, no implica necesariamente que sean idénticos."""
#compara el valor entre las variuables 
a = 3
b = 3  
c = 4
print (a is b) # muestra True
print (a is not b) # muestra False
print (a is not c) # muestra True


#x es una variable mutable cambia de valor de x a y a z 
x = 1
y = x
z = y
print (z is 1) # muestra True
print (z is x) # muestra True


str1 = "FreeCodeCamp"
str2 = "FreeCodeCamp"

print (str1 is str2) # muestra True
print ("Code" is str2) # muestra False

a = [10,20,30]
b = [10,20,30]

print (a is b) # muestra False (ya que las listas son objetos mutables en Python)  

#bucle o ciclo (while)

"tiene un nuero indeterminado de ejecuciones"
while numero <= 10:
    suma = numero + suma
    numero = numero + 1
print ("La suma es " + str(suma))




