Monto = 10000
Ope= ["Retirar","Ver saldo","Salir"]
O=[20,50,100,150,500,"Otro Monto"]
P=[1,2,3,4,5,6]
i=0
y=1
while i<10:
    clave= input("Introduzca su clave: ")
    if clave == "1313":         #comprobamos que la clave es correcta
        while True:
            print("--------------Menu--------------")
            for op in Ope:  #creamos un bucle con todas las opciones
                print(op,"(",P[i],")")
                i+=1        
            i=0
            try:
                E=int(input("¿Que operación desea realizar?: "))    
            except:
                print("Porfavor escriba una opción válida.")        #si la opcion escogida no es un entero, saldra el mensaje.
                continue
            if E == 1:
                print ("-------------Retiro-------------")
                for d in O:                          #creamos un bucle con las opciones de retiro
                    print (d,"(",P[i],")")
                    i+=1
                i=0
                try:
                    retiro=int(input("Elige un número: ")) 
                except:
                    print("No existe esa opción.")          #si la opcion escogida no es un entero, saldra el mensaje.
                    continue
                if retiro <6:         #Este condicional se activa cuando el retiro es una de las primeras 5 opciones
                    if Monto - O[retiro-1] > 0:
                        Monto = Monto - O[retiro-1]
                        print("-"*32)
                        print ("Su saldo restante es: ",Monto)
                    else:
                        print("-"*32)
                        print("Usted no cuenta con saldo suficiente.")
                        continue
                elif retiro == 6:           #Si el cliente escoge "Otro monto", se activa esta condicional
                    try:
                        retiro = int(input("Cuanto quieres retirar?: "))
                    except:
                        print("-"*32)
                        print("Valor no valido. Operación cancelada")       #Si el cliente introduce un valor que no sea un entero, la operación se cancela
                        continue
                    if retiro == 0 or retiro > Monto:
                        print("La operación falló. El retiro no puede ser de 0 soles o usted no cuenta con el saldo necesario.")
                        continue
                    else:    
                        Monto=Monto-retiro
                        print("-"*32)
                        print("Su saldo restante es: ",Monto)
                else:
                    print("No existe esa opción.")      #Esto pasa cuando el valor introducido en el RETIRo es un entero pero no una opción.
                    continue
            elif E ==2:
                print("-"*32)
                print("Su saldo es de: ",Monto)
            elif E==3:
                print("-"*32)
                print("Gracias por usar este cajero.")
                i+=100
                break
            else:
                print("-"*32)
                print("Porfavor escriba una opción válida.")   #Esto pasa cuando el valor introducido en el MENU es un entero, pero no es parte de las opciones.
    else:
        if y>-1:
            print("Clave incorrecta, le quedan",P[y],"intento(s).")
            y-=1
        else:
            print("Demasiados intentos fallidos, su tarjeta fue retenida.")
            break