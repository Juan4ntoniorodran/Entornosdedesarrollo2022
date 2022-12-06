genero= input("Introduzca su género")
while genero!="H" and genero!="M":
    genero= input("Introduzca un género correcto")

edad= int(input("Introduzca su edad"))
while edad<23 or edad>65:
    edad= int(input("Introduzca una edad válida"))

fumador= input("Es usted fumador")
while fumador!="S" and fumador!="N":
    fumador= input("Por favor, responda S o N")
    
canthombres=0
cantmujeres=0
mediaedad=edad+edad