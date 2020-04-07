import math
"""
Created on Tue Apr  7 11:58:16 2020

@author: Julian
"""
"""
cad= str(chr(97))
print(cad)

tan= ord(cad)

print(tan)

"""

z = 2


cad= str(input("ingrese: Usuario,Contraseña: "))
cad = (cad.split(','))
# cad= list(cad)
o = open("ENTLC.txt",'r+') 
lec= o.readlines()

for i in lec:
    lectura = i.split(',')
    if lectura[0] == cad[0]:
        print("Confirmo 1005% REAL, NO FAKE")

# # ---- los caracteres ingresados y devuelve su valor en el codigo ascii ----
# i=0
# while i< len(cad):  
#     cad[i] = ord(cad [i])
#     print(cad[i])
#     i=i+1


# ----imprime la posicion encriptada del numero en la posicion ----
    
vi = list(range(len(cad)))

o.close()

# #  ---- encripta el archivo ----

# i=0
# while i< len(cad):      
#     vi[i] = ( cad[i] +(cad[i]*cad[i]) )
#     # print(vi[i])    
#     i=i+1

# i=0

# # ---- desenpripta el archivo ----
# des=""
# while i< len(cad):
#     ve= vi[i]-(cad[i]*cad[i])
#     # print(chr(ve))
#     des = des + str(chr(ve))
#     i=i+1
# print(des)

# ---- abre archivo y lee lineas ----
    
# o = open("ENTLC.txt",'r+') 

# lec= o.readlines()

# for i in lec:
#     print(i.split(','))
# print()

# o.write("\n"+"suPutaMadre")
# o.close()


