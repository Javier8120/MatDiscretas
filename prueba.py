

error=False
x = int(input("Digite la parte entera del decimal: "))
if x == 0 :
    print("Oee, solo estamos trabajando con numeros mayores a 0")
elif x < 0 :
    error=True
if error==True:
    print ("Oee, tamos trabajando con numeros racionales, intenta nuevamente")
else:
    y = int(input("Digite el periodo del numero decimal: "))
    if y < 0:
        print("Ehhh recuerde que los decimales no son negativos x.x")
    elif y == 0:
        print(":V Acaso hay decimales periodicos que solo tengan 0 *_* ")
    else:
        lista=[9, 99, 999, 9999, 99999, 999999]
            
        if y < 10 and y > 0:
            numerador=lista[0]
        elif y < 100 and y >= 10:
            numerador=lista[1]
        elif y < 1000 and y >= 100:
            numerador=lista[2]
        elif y < 10000 and y >= 1000:
            numerador=lista[3]
        elif y < 100000 and y >= 10000:
            numerador=lista[4]
        elif y < 1000000 and y >= 100000:
            numerador=lista[5]
        else:
            error2=True
        
if error2 == True:
   print("Tas pasandote de lanza :v, Solo trabajamos los decimales posibles entre 1 y 99999")
else:        
     denominador = int(f"{x}{y}")
     denominador_fraccion = (denominador-x)
     print ("La fraccion resultante de :",denominador_fraccion/numerador, "es:",denominador_fraccion,"/",numerador)




#print(b)