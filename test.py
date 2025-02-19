#Program 1
#Declare your age as integer variable
print("Ingresa tu edad: ")
edad=18
print(type(edad))
print(int(edad))
###############################################################################
# Program 2 
#Declare your height as a float variable
print("Ingresa tu estatura")
Heigth= 1.65
print(type(Heigth))
print(float(Heigth))
###############################################################################
#Program 3
#Declare a variable that store a complex number
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
################################################################################
#Program 4 
#Write a scrip that prompts the yuser to enter base and height
# of the trangle and calculate an area of this triangle 
# (area= 0.5 x b x h)
base= float(input("ingresa el valor de la base: "))
altura= float(input("ingresa el valor de la altura: "))
area= (0.5 * base * altura)
print("El area del triangulo es: " + str(area))
##################################################################################
#Program 5
#write a crop that promots to enter side a, side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
slidea= float(input("enter the lide a: "))
slideb= float(input("enter the slide b: "))
slidec= float(input("enter the slide c: "))
area=(slidea + slideb + slidec)
print("el perimetro del triangulo es de: " + str(area))
###################################################################################
#Program 6
#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
ancho= float(input("ingresa el ancho: "))
largo= float(input("ingresa la altura: "))
area= (largo * ancho)
perimetro=(2*(largo + ancho))
print ("la longuitud del rectangulo es de: " + str(largo))
print("la anchura del rectangulo es de: " + str(ancho))
###################################################################################
#Program 7
#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radio= int (input("ingresa el radio del circulo:"))
pi= 3.14159
areaOfCircle= pi * radio ** 2
circumOfCircle= 2 * pi* radio
print("The area of the circle is ", areaOfCircle)
print("The circumference of the circle is ", circumOfCircle)
print("el radio del circulo es: " + str(radio))
###################################################################################
#Program 8
#Calculate the slope, x-intercept and y-intercept of y = 2x -2
