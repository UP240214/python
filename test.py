#Program 1
#Declare your age as integer variable
print("Ingresa tu edad: ")
edad=18
print(type(edad))
print(int(edad))
print("")
###############################################################################
# Program 2 
#Declare your height as a float variable
print("")
print("Ingresa tu estatura")
Heigth= 1.65
print(type(Heigth))
print(float(Heigth))
print("")
###############################################################################
#Program 3
#Declare a variable that store a complex number
print("")
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
print("")
################################################################################
#Program 4 
#Write a scrip that prompts the yuser to enter base and height
# of the trangle and calculate an area of this triangle 
# (area= 0.5 x b x h)
print("")
base= float(input("ingresa el valor de la base: "))
altura= float(input("ingresa el valor de la altura: "))
area= (0.5 * base * altura)
print("El area del triangulo es: " + str(area))
print("")
##################################################################################
#Program 5
#write a crop that promots to enter side a, side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
print("")
slidea= float(input("enter the lide a: "))
slideb= float(input("enter the slide b: "))
slidec= float(input("enter the slide c: "))
area=(slidea + slideb + slidec)
print("el perimetro del triangulo es de: " + str(area))
print("")
###################################################################################
#Program 6
#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
print("")
ancho= float(input("ingresa el ancho: "))
largo= float(input("ingresa la altura: "))
area= (largo * ancho)
perimetro=(2*(largo + ancho))
print ("la longuitud del rectangulo es de: " + str(largo))
print("la anchura del rectangulo es de: " + str(ancho))
print("")
###################################################################################
#Program 7
#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
print("")
radio= int (input("ingresa el radio del circulo:"))
pi= 3.14159
areaOfCircle= pi * radio ** 2
circumOfCircle= 2 * pi* radio
print("The area of the circle is ", areaOfCircle)
print("The circumference of the circle is ", circumOfCircle)
print("el radio del circulo es: " + str(radio))
print("")
###################################################################################
#Program 8
#Calculate the slope, x-intercept and y-intercept of y = 2x -2
print("")
print("interaccion  de la pendiente" )
pendiente= 2 ##la pendiente de la eccuacion
inty= -2 ##interaccion con eje y 
intx= inty / pendiente ##interaccion con eje x
print("la pendeinte de la eccuacion es: ", pendiente)
print("la interaccion es de: ", intx)
###################################################################################
#Program 9
#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
print("")
x1=2 
x2= 6
y1=2
y2=10
distance= ((x2- x1)**2 + (y2 - y1)**2)**0.5
print("la distancia entre los dos puntos es: ", distance)
slope=(y2 - y1)/(x2 - x1)
print("The slope is: ", slope)
print("")
###################################################################################
#Program 10
print("")
###################################################################################
#Program 11
print("")
vax= int(input("ingresa el valor de x "))
vay= (vax**2 +(6* vax) + 9)
print("el valor de la variable y es igual a ", "|", vay, "|")
print("")
#####################################################################################
#Program 12
print("")

word1 = "python"
word2 = "dragon"

dist1 = len(word1)
dist2 = len(word2)


print(f"Length of '{word1}':", dist1)
print(f"Length of '{word2}':", dist2)


comparasionFalsa = dist1 > dist2 and dist1 < dist2
print("comparacion falsa:", comparasionFalsa)
########################################################################################
#Program 13
print("")
word1 = "python"
word2 = "dragon"
if "on" in word1 and "on" in word2:
    print("'on' se encuentra en ambas palabras.")
else:
    print("'on' no se encuentra en ambas palabras.")
print("")
######################################################################################
#Program 14
wordd= "I hope this course is not full of jargon"
if "jargon" in wordd:
    print("Jargon se encuentra en la oracion")
else:
    print("jargon no se encuentra en la oracion")
print("")
######################################################################################
#Program 15
print("")
word1 = "python"
word2 = "dragon"
if "on" in word1 and "on" in word2:
    print("'on' no se encuentra en ambas palabras.")
else:
    print("'on' no se encuentra en ambas palabras.")
print("")
######################################################################################
#Program 16
print("")
word16= "python"
dist16= len(word16)
print(float(dist16))
print(str(dist16))
print("")
#######################################################################################
#Program 17
num= int(input("ingresa un numero: "))
if num % 4 ==0:
 print("el numero es par")
else:  
   print("el numero es impar")
print("")
 #######################################################################################
#Program 18
#7/3=2.77
num1= 7
num2= 3
div= num1/ num2

if div== 2.7:
 print("es correcta la suposicion")
else:
 print("es incorrecta la suposicion, en realidad es: " , div)
print("")
#######################################################################################
#Program 19
if type("10")==type(10):
 print("es verdadero son iguales")
else: 
   print("es falso, no son iguales")
print("")
##########################################################################################
#Program 20
if float('9.8')==type(10):
    print("es verdadero son iguales")
else: 
   print("es falso, no son iguales")
print("")
#########################################################################################
#Program 21
print("bienvenido")
tiempo=int(input("ingresa las horas que has estado: "))
print("la tarifa por hora es de $17 por hora")
tarifaTotal= tiempo * 17
print("el total a pagar es de: " , tarifaTotal)
print("")
#########################################################################################
#Program 22
edad=int(input("Escriba su edad: "))
segundosHora= 3600
segundosDia= segundosHora * 24
SegundosMes= segundosDia * 30
segundosAño= SegundosMes * 12
Total= segundosAño * edad
print(Total)
print("")
#########################################################################################
#Program 23
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 24 125")
print("")
#########################################################################################












