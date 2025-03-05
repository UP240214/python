#Program 1
print("")
print("EJERCISE 1:")
word1= "thirty"
word2= " days"
word3= " of"
word4=" python"
completeSentence= word1 + word2 +word3 +word4 
print(completeSentence)
print("")
###############################################################################
#program 2

print("EJERCISE 2:")
fir1="Coding"
sec1=" for "
ter1="all"
com1= fir1 + sec1 + ter1
print(com1)
print("")
################################################################################
#Program 3
print("EJERCICIO 3: ")
company= com1
print("")
################################################################################
#Program 4
print("EJERCICIO 4: ")
print(company)
print("")
################################################################################
#Program 5
word5= "company"
dist= len(word5)
print(f"Length of '{word5}':", dist)
print("")
#################################################################################
#Program 6
word5= "company"
print("Texto en mayúsculas:", word5.upper())
print("")
##################################################################################
#Program 7
word5= "company"
print("Texto en mayúsculas:", word5.lower())
print("")
##################################################################################
#Program 8
sentence= "Coding for all"
print("capitalize():", sentence.capitalize())  # Primera letra en mayúscula
print("title():", sentence.title())  # Primera letra de cada palabra en mayúscula
print("swapcase():", sentence.swapcase())  # Invierte mayúsculas y minúsculas
print("")
##################################################################################
#Program 9
sentence= "Coding for all"
print("Sin la primera palabra:", sentence[sentence.find(" ") + 1:])
print("") 
##################################################################################
#Program 10
subcadena=sentence
print(subcadena.find("codificacion"))
print("")
##################################################################################
#Program 11
sentence11= "for all"
word11= "Coding "
print(word11 + sentence11)
print("")
##################################################################################
#Program 12
word12= "Python for Everyone "
wrdreplace="all"
newword= word12.replace("Everyone", "all")
print(newword)
print("")
##################################################################################
#Program 13
word13 = "Coding For All"
newword13 = word13.split(" ")
print(newword13)
print("")
##################################################################################
#Program 14
word14= "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
newword14 = word14.split(" ")
print(newword14)
print("")
##################################################################################
#Program 15
word15 = "Coding For All"
newword15= word15[0]
print(newword15)
print("")
#################################################################################
#Program 16
word16 = "Coding For All"
newword16 = len(word16) -1
print(newword16)
print(word16[-1])
print("")
#################################################################################
#Program 17
word17 = "Coding For All"
newword17 = word17[10]
print(newword17)
print("")
##################################################################################
#Program 18
word18= "Python For Everyone"
PPP=word18[0]
FFF=word18[7]
EEE=word18[11]
print(PPP,FFF,EEE)
print("")
##################################################################################
#Program 19
word19= "Coding For All"
w191=word19[0]
w192=word19[7]
w193=word19[11]
print(w191,w192,w193)
print("")
##################################################################################
#Program 20
word20 = "Coding For All"
print(word20.find("C"))
print("")
##################################################################################
#Program 21
word20 = "Coding For All"
print(word20.find("F"))
print("")
##################################################################################
#Program 22
word22 = "Coding For All"
rfindwrd = word22.rfind("l")
print(rfindwrd)
print("")
##################################################################################
#Program 23
word23= "You cannot end a sentence with because because because is a conjunction"
indexword= word23.index("because")
print(indexword)
print("")
##################################################################################
#Program 24
word24 = "You cannot end a sentence with because because because is a conjunction"
rindeswrd = word24.rindex("because")
print(rindeswrd)
print("")
##################################################################################
#Program 25
word25 = "You cannot end a sentence with because because because is a conjunction"
start = word25.find("because because because")
lenwrd= start + len("because because because")
print("Start", start)
print("final: ", lenwrd)
newStr = word25[0:start] + word25[lenwrd:]
print(newStr)
print("")
###################################################################################
#Program 26
word26 = "You cannot end a sentence with because because because is a conjunction"
start26 = word26.find("because")
print("POSITION:")
print(start26)
final26 = start + len("because")
print(final26)
newstr26= word26[0:31] + word26[38:]
print(newstr26)
print("")
#####################################################################################
#Program 27
word25 = "You cannot end a sentence with because because because is a conjunction"
start = word25.find("because because because")
lenwrd= start + len("because because because")
print("Start", start)
print("final: ", lenwrd)
newStr = word25[0:start] + word25[lenwrd:]
print(newStr)
print("")
######################################################################################
#Program 28
str28 = "Coding For All"
startstr26 = str28.find("Coding")
print(startstr26)
if startstr26 == 0:
 print("es correcto")
else:
 print("Es incorrecto")
print("")
######################################################################################
#Program 29
str28 = "Coding For All"
startstr26 = str28.find("coding")
print(startstr26)
if startstr26 == 0:
 print("es correcto")
else:
 print("Es incorrecto")
print("")
######################################################################################
#Program 30
str30 = " Coding For All "
start30 = str30.find(" ")
print(start30)
final30 = start30 + len("Coding For All")
print(final30)
newstr30 = str30[1:16]
print(newstr30)
print("")
#######################################################################################
#Program 31
str31 = "30DaysOfPython"
print (str31.isidentifier())
str312 = "thirty_days_of_python"
print(str312.isidentifier())
print("")
########################################################################################
#Program 32