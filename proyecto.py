import random

# clave=1234
# dni = 12345678
clave=1
dni = 1
dni_ingresado = 0
reintentos=0
opcion_menu_principal=0
mensaje_menu_principal = "\n--------------- \n1. Consultas \n2. Retiros \n3. Transferencias \n4. Salir \n--------------- \nelija opcion >> "
mensaje_menu_opcion_1 = "\n--------------- \nA - Posicion Global \nB - Movimientos \n--------------- \neliga opcion >> "
# mensaje_menu_opcion_2 = "\n--------------- \n Seleccione el tipo de moneda\nA - Pesos \nB - Soles \nC - volver \n--------------- \nelija opcion >> "
mensaje_menu_opcion_3 = "\n--------------- \nA - Indique numero de cuenta destino \nB - volver  \n--------------- \nelija opcion >> "
saldo_pesos = 85000
saldo_soles = 3564
moneda_elegida= 0
regresiva = 10
gastos=['INGRESO - DEPOSITO','EGRESO - SUPERMERCADO','EGRESO - CARNICERIA','EGRESO - EXTRACCION','EGRESO - RESTAURANTE','EGRESO - ZAPATERIA','EGRESO - TRANSFERENCIA','EGRESO - MASCOTERIA','INGRESO - TRANSFERENCIA','EGRESO - FARMACIA']
tipo_de_moneda= "-------------\nA.Pesos\nB.Soles\n------------ \nSeleccione el tipo de moneda>> "

# ------------------------------
def seleccionar_moneda():
  moneda=' '
  eleccion=True

  while eleccion:
    opcion=input(tipo_de_moneda)
    if opcion=='A':
      moneda='Pesos'
      eleccion=False
    if opcion=='B':
      moneda='Soles'
      eleccion=False

  return moneda
# ------------------------------
def confirma(texto):
  texto_impresion= f"Desea {texto} Si o No (S/N):"
  opcion=' '
  eleccion=True

  while eleccion:
    opcion=input(texto_impresion)
    if opcion=='S':
      eleccion=False
    if opcion=='N':
      eleccion=False
  
  return opcion
# ------------------------------
def menu_opcion_1(opcion_menu_principal):
  while opcion_menu_principal == 1:
    opcion_ingresada=input(mensaje_menu_opcion_1)

    if opcion_ingresada is "A": # Posicion Global o Saldo
      moneda_elegida = seleccionar_moneda()
      if moneda_elegida=='Pesos':
        if confirma('imprimir') == "N":
          print(f"Su saldo disponible en {moneda_elegida} es de: ${saldo_pesos}")
        else:
          print("Su comprobante de Saldo se esta imprimiendo ...")
      elif moneda_elegida=='Soles':
        if confirma('imprimir') == "N":
          print(f"Su saldo disponible en {moneda_elegida} es de: ${saldo_soles}")
        else:
          print("Su comprobante de Saldo se esta imprimiendo ...")

      opcion_menu_principal=0
    elif opcion_ingresada is "B": # Movimientos (al azar)
      moneda_elegida = seleccionar_moneda()
      if confirma('imprimir') == "N": 
        print(f"Sus moviminetos en {moneda_elegida} son:")
        for i in range(10):
          print(f"--->  {gastos[random.randint(0,9)]} : ${round(random.uniform(0.00, 999999.99),2)}")
      else:
        print("Su comprobante de Saldo se esta imprimiendo ...")
      
      opcion_menu_principal=0
    else:
      print("opcion no valida")


while reintentos<3 and opcion_menu_principal!=4 and dni_ingresado==0:
  clave_ingresada= int(input(" ingrese su clave: "))   
  if clave_ingresada != clave:     #si la clave no es correcta
    print(f"La clave ingresada {clave_ingresada}, no es valida")
    reintentos+=1 
  else:    #cuando la clave es correcta
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
      # Ejecuto el Menu de la Opcion 1
      menu_opcion_1(opcion_menu_principal)

      # ------------------------------
      # Menu Opcion 2
      #
      while opcion_menu_principal == 2:
        # opcion_ingresada=input(mensaje_menu_opcion_2)
        moneda_elegida = seleccionar_moneda()
        if moneda_elegida=='Pesos':
          monto_a_retirar = int(input("Ingrese monto a retirar: "))
          if monto_a_retirar > saldo_pesos:    #si el monto a retirar es mayor que el saldo
            print(f"el monto {monto_a_retirar} a retirar exede el saldo: {saldo_pesos}")
            if confirma('salir') == "S":
              opcion_menu_principal=0
            else:
              monto_a_retirar = int(input("Ingrese monto a retirar: "))
              if monto_a_retirar > saldo_pesos:
                opcion_menu_principal=0
          else:     # si se verifica la disponibilidad de saldo
            clave_ingresada= int(input(" ingrese su clave: "))
            if clave_ingresada != clave: 
              print(f"La clave ingresada {clave_ingresada}, no es valida")
            else:
              monto_a_retirar-=saldo_pesos
              if confirma('imprimir') == "N": 
                print("Transaccion realizada con exito:")
                opcion_menu_principal=0
              else:
                print("Su comprobante de Saldo se esta imprimiendo ...")
                opcion_menu_principal=0

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
    #import time 
    #while regresiva > 0: 
    #  print (f'Retire su tarjeta en {regresiva}') 
    #  regresiva-=1
    #  time.sleep(1)
    #print("ups! el cajero se comio tu tarjeta \nla proxima hay que ser mas rapidos :)")


    
