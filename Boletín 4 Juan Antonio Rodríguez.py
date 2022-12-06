# 1. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
from math import sqrt
catmenor= int(input("Introduzca las dimensiones del cateto menor"))
catmayor= int(input("Introduzca las dimensiones del cateto mayor"))
hipotenusa= sqrt(catmayor**2+catmenor**2)

print(hipotenusa)

# 2. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius
temperatura= int(input("Introduzca la temperatura"))
gradosfarenheit= (temperatura*1.8)+32
print (gradosfarenheit)

# 3. Calcular la media de tres números pedidos por teclado.
numero1= int(input("Introduzca el primer número"))
numero2= int(input("Introduzca el segundo número"))
numero3= int(input("Introduzca el tercer número"))
media= (numero1+numero2+numero3)/3
print ("La media es: ",media)

# 4. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
# cuanto deberá pagar finalmente por su compra.

precioinicial= int(input("Introduzca el precio total de su compra"))
descuento=precioinicial*0.15
preciototal= precioinicial-descuento
print ("Usted deberá pagar: ",preciototal,"€")

# 5. Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
# diferencia, de modo que el resultado sea siempre positivo).
numero1= int(input("Introduzca el primer número"))
numero2= int(input("Introduzca el segundo número"))
absoluto= abs(numero1-numero2)
print ("La distancia entre ambos números es: ",absoluto)

# 6.

# 7. Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
#Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se
#puede calcular?

import math
num= int(input("Introduzca un número"))
raizcuad= math.sqrt(num)
raizcub= num**(1/3)
print (raizcuad)
print (raizcub)

# 8. 

# 9. . Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
#exponente. Pueden ocurrir tres cosas:
#◦ El exponente sea positivo, sólo tienes que imprimir la potencia.
#◦ El exponente sea 0, el resultado es 1.
#◦ El exponente sea negativo, el resultado es 1/potencia con el exponente positivo

base= int(input("Introduzca la base"))
exponente= int(input("Introduzca el exponente"))
potencia= 0

if exponente>0:
    potencia= base**exponente
    print (potencia)
elif exponente==0:
    potencia=1
    print (potencia)
elif exponente<0:
    potencia= 1/base**(exponente*(-1))
    print (potencia)

# 10.. Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
#lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en
#cuenta los siguiente:
#◦ Si se cumple Pitágoras entonces es triángulo rectángulo
#◦ Si sólo dos lados del triángulo son iguales entonces es isósceles.
#◦ Si los 3 lados son iguales entonces es equilátero.
#◦ Si no se cumple ninguna de las condiciones anteriores, es escaleno

import math
medida1= int(input("Introduzca el primer dato"))
medida2= int(input("Introduzca el segundo dato"))
medida3= int(input("Introduzca el tercer dato"))
pitagorasa= medida3**2-medida2**2
pitagorasb= medida3**2-medida1**2
pitagorasc= medida1**2+medida2**2

if medida1== math.sqrt(pitagorasa) or medida2== math.sqrt(pitagorasb) or medida3== math.sqrt(pitagorasc):
    print ("El triángulo es Rectángulo")
elif medida1==medida2 or medida1==medida3 or medida2==medida1 or medida2==medida3 or medida3==medida1 or medida3==medida2:
    print ("El triángulo es isósceles")
elif (medida1==medida2 and medida1==medida3) or (medida2==medida3 and medida2==medida1) or (medida3==medida1 and medida3==medida2):
    print ("El triángulo es equilátero")
else:
    print ("El triángulo es escaleno")

# 11.Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un
# número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible
# por 400.

año= int(input("Introduzca un año"))
if año%4==0 or año%400==0 or año%100==0:
    print ("El año es bisiesto")
else:
    print ("El año es biniesto")

# 12.. La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual
#se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del
#producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
#productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
#se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de
#tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
#cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida

precioinicial= int(input("Introduzca el precio inicial del kilo de uva"))
tipo= input("Introduzca el tipo de uva (A o B)")
tamaño= input("Introduzca el tamaño de la uva (1 o 2)")
preciototal= 0

if tipo=="A":
    if tamaño==1:
        preciototal= precioinicial+0.20
        print ("El precio del kilo de uva será: ",preciototal)
    else:
        preciototal= precioinicial+0.30
        print ("El precio del kilo de uva será: ",preciototal)
elif tipo=="B":
    if tamaño==1:
        preciototal= precioinicial-0.30
        print ("El precio del kilo de uva será: ",preciototal)
    else:
        preciototal= precioinicial-0.50
        print ("El precio del kilo de uva será: ",preciototal)

# 13.
# 14.
# 15. Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día
#correspondiente. Si introducimos otro número nos da un error.

dia= int(input("Introduzca un número del 1 al 7"))

if dia== 1:
    print ("Lunes")
elif dia==2:
    print ("Martes")
elif dia==3:
    print ("Miércoles")
elif dia==4:
    print ("Jueves")
elif dia==5:
    print ("Viernes")
elif dia==6:
    print ("Sábado")
elif dia==7:
    print ("Domingo")
else:
    print ("Por favor, introduzca un número válido")
    
# 16. Escribe un programa que pida un número entero entre uno y doce e imprima el número de
# días que tiene el mes correspondiente
num= int(input("Introduzca un número del 1 al 12"))

if num==1 or num==3 or num==5 or num==7 or num==9 or num==11:
    print ("El mes tiene 30 días")
elif num==2:
    print ("El mes tiene 28 días")
else:
    print ("El mes tiene 31 días")



