clave=1234
dni = 12345678
dni_ingresado = 0
reintentos=0
opcion_menu_principal=0
mensaje_menu_principal = "\n--------------- \n1. .... \n2. .... \n3. ..... \n4. .... \n--------------- \neliga opcion >> "
mensaje_menu_opcion_1 = "\n--------------- \nA - Posicion Global \nB - Movimientos \nC - volver \n--------------- \neliga opcion >> "

#hay que cambiar el contenido de estos mensajes por los que corresponden a la opcion 2 y 3
mensaje_menu_opcion_2 = "\n--------------- \nA - Posicion Global \nB - Movimientos \nC - volver \n--------------- \neliga opcion >> "
mensaje_menu_opcion_3 = "\n--------------- \nA - Posicion Global \nB - Movimientos \nC - volver \n--------------- \neliga opcion >> "

regresiva = 10
    
while reintentos<3 and opcion_menu_principal!=4 and dni_ingresado==0:
  clave_ingresada= int(input(" ingrese su clave: "))   
  if clave_ingresada != clave:  #si la clave no es correcta
    print(f"La clave ingresada {clave_ingresada}, no es valida")
    reintentos+=1
  else: #cuando la clave es correcta
    dni_ingresado = int(input(" ingrese su dni: "))
    while dni_ingresado != dni:     #si lel dni no es correcto
      print(f"El nro de DNI ingresado {dni_ingresado}, no es valido")
      dni_ingresado = int(input(" ingrese su dni: "))
  if clave_ingresada== clave and dni_ingresado==dni:
    # ------------------------------
    # Menu Principal
    #
    while opcion_menu_principal!=4:
      opcion_menu_principal = int(input(mensaje_menu_principal))

      # ------------------------------
      # Menu Opcion 1
      #
      while opcion_menu_principal == 1:
          opcion_ingresada=input(mensaje_menu_opcion_1)
          if opcion_ingresada is "A":
            print("show posicion global") #todavia no hace nada 
          elif opcion_ingresada is "B":
            print("show movimientos") #todavia no hace nada
          elif opcion_ingresada is "C":
            opcion_menu_principal=0
          else:
            print("opcion no valida")

      # ------------------------------
      # Menu Opcion 2
      #
      while opcion_menu_principal == 2:
          opcion_ingresada=input(mensaje_menu_opcion_2)
          if opcion_ingresada is "A":
            print("show posicion global") #todavia no hace nada 
          elif opcion_ingresada is "B":
            print("show movimientos") #todavia no hace nada
          elif opcion_ingresada is "C":
            opcion_menu_principal=0
          else:
            print("opcion no valida")

      # ------------------------------              
      # Menu Opcion 3
      #
      while opcion_menu_principal == 3:
          opcion_ingresada=input(mensaje_menu_opcion_3)
          if opcion_ingresada is "A":
            print("show posicion global") #todavia no hace nada 
          elif opcion_ingresada is "B":
            print("show movimientos") #todavia no hace nada
          elif opcion_ingresada is "C":
            opcion_menu_principal=0
          else:
            print("opcion no valida")

    # ------------------------------              
    # Cuenta regresiva
    # no es necesario pero me parecio piola
    import time 
    while regresiva > 0: 
      print (f'Retire su tarjeta en {regresiva}') 
      regresiva-=1
      time.sleep(1)
    print("ups! el cajero se comio tu tarjeta \nla proxima hay que ser mas rapidos :)")

    