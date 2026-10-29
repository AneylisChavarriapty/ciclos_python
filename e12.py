s=9
intento =int(input("Adivina el numero del (1 al 10):"))

while intento !=s:
    if intento <s:
        print("Muy bajo")
    else:
        print("Muy alto")
    intento= int(input("Intenta de nuevo:"))
print ("¡Acertaste!")