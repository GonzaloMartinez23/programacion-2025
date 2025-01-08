# nombre="Gonzalo Martinez"
# edad=33
# print("mi nombre es ",nombre, "y mi edad es " , edad)

# num1=0
# num2=0

# print("Ingrese un primer numero") 
# num1 = int(input())  
# print("Ingrese un segundo numero") 
# num2 = int(input())  


# print(num1+num2)
#------------------------------------------------------

# print("Ingrese un primer numero") 
# num1 = int(input())  
# if  num1>0:
#     print("El numero es positivo")
# else:   
#     print("El numero es negativo o cero") 

# print("Ingrese su edad") 
# edad = int(input())  
# if  edad >= 18:
#     print("usted es mayor de edad")
# else:   
#     print("usted es menor de edad") 
    
#------------------------------------------------------
 
# print("Ingrese un numero") 
# num1 = int(input())  
# print("Ingrese un segundo numero") 
# num2 = int(input())  
# print("Ingrese un tercer numero") 
# num3 = int(input())  

# print((num1+num2+num3)/3)
#------------------------------------------------------


print("**BIENVENIDO AL PARQUE NACIONAL**")
print("cual es su edad?")
edad=int(input())

if edad < 12:
    print("valor de la entrada es $500")  
    print("cuantas entradas necesita?") 
    cantidad=int(input())
    total=(cantidad*500)
    print("el total a pagar es ",total)
    
elif edad >= 13 and edad <= 18:
    print("valor de la entrada es $1000")
    print("cuantas entradas necesita?") 
    cantidad=int(input())
    total=(cantidad*1000)
    print("el total a pagar es ",total)
    
elif edad >= 19 and edad <= 64:
    print("valor de la entrada es $2000")
    print("cuantas entradas necesita?") 
    cantidad=int(input())
    total=(cantidad*2000)
    print("el total a pagar es ",total)    
else:
    print("valor de la entrada es $700")
    print("cuantas entradas necesita?") 
    cantidad=int(input())
    total=(cantidad*700)
    print("el total a pagar es ",total)
  
  #------------------------------------------------------  
  
print("pertenece a la florida? si o no")
respuesta=input()   
if respuesta == "si":
    print("usted es de la florida")
    print("tiene carnet de la florida? si o no")
    respuesta=input()
    if respuesta == "si":
        print("ingrese su numero de carnet de socio")
        carnet=input()
    if respuesta == "no":
        print("creese un carnet de socio aca")
    
    print("es usted jubilado? si o no")
    if respuesta == "si":
        print("tiene descuento del 25%")
        print(("su total con descuento es : "), total*0.75)  
    if respuesta == "no":
        print("no tiene descuento")
        print("su total es : ",total)   
        
       
       
       
print("gracias por visitar la florida")

