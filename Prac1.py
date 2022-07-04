print ("practica1")
num = int(input("ingresa un numero desde -inf hasta +inf: \n"))
if(num <0):
    print("Tu numero es negativo")
else:
    print("Tu numero es positivo")

parOimpar = int(input("Ingrese un numero para conocer si es par o impar:"))
if(parOimpar % 2 == 0):
    print("Numero par")
else:
    print("Numero impar")

#menor o mayor de tres numeros 
a = int(input("ingrese un numero "))
b = int(input("ingrese un numero "))
c = int(input("ingrese un numero "))
if a > b and a>c:
    print ("el mayor es",a)
if b > a and b >c:
    print ("el mayor es",b)
if c > a and c >b:
    print ("el mayor es",c)
if a < b and a<c:
    print ("el menor es ",a)
if b < a and b<c:
    print ("el menor es",b)
if c < a and c<b:
    print ("el menor es",c)