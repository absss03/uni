

import random

# clave=1234
# dni = 12345678
clave=1
clave_ingresada=0
dni = 1
dni_ingresado = 0

opcion_menu_principal=0
mensaje_menu_principal = "\n--------------- \n1. Consultas \n2. Retiros \n3. Transferencias \n4. Salir \n--------------- \nelija opcion >> "
mensaje_menu_opcion_1 = "\n--------------- \nA - Posicion Global \nB - Movimientos \n--------------- \neliga opcion >> "
mensaje_menu_opcion_3 = "\n--------------- \nA - Indique numero de cuenta destino \nB - volver  \n--------------- \nelija opcion >> "
gastos=['INGRESO - DEPOSITO','EGRESO - SUPERMERCADO','EGRESO - CARNICERIA','EGRESO - EXTRACCION','EGRESO - RESTAURANTE','EGRESO - ZAPATERIA','EGRESO - TRANSFERENCIA','EGRESO - MASCOTERIA','INGRESO - TRANSFERENCIA','EGRESO - FARMACIA']
tipo_de_moneda= "-------------\nA.Pesos\nB.Soles\n------------ \nSeleccione el tipo de moneda>> "
moneda_elegida= 0
saldo_pesos = 85000
saldo_soles = 3564
saldo= 0
cuenta = 98765
cuenta_ingresada = 0
regresiva = 10
devolucion= 0


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
def solicitar_clave():
  clave_aceptada=False
  reintentos=0

  while reintentos<3 and not clave_aceptada:
    clave_ingresada= int(input("ingrese su clave: "))   
    if clave_ingresada != clave:     #si la clave no es correcta
      print(f"La clave ingresada {clave_ingresada}, no es valida")
      reintentos+=1
    else:
      clave_aceptada=True

  return clave_aceptada
# ------------------------------
def solicitar_dni():
  dni_aceptado=False

  while not dni_aceptado:     #si lel dni no es correcto
    dni_ingresado = int(input("ingrese su dni: "))
    if dni_ingresado != dni:
      print(f"El nro de DNI ingresado {dni_ingresado}, no es valido")
    else:
      dni_aceptado=True

  return dni_aceptado
# ------------------------------
def retira_monto(saldo, moneda_elegida):
  monto_a_retirar = int(input("Ingrese monto a retirar: "))     #Pide el monto a retirar
  if monto_a_retirar <= saldo:
    if solicitar_clave():
      saldo-=monto_a_retirar
      if confirma('imprimir') == "N":
        print("Transaccion realizada con exito")
      else:
        print("Su comprobante de Saldo se esta imprimiendo ...")
    else:
      saldo=0
  else:
    print(f"el monto {monto_a_retirar} a retirar en {moneda_elegida} exede el saldo: {saldo}")
 
  return saldo
# ------------------------------
def menu_opcion_1():
  opcion_ingresada=input(mensaje_menu_opcion_1)

  if opcion_ingresada == "A": # Posicion Global o Saldo
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

  elif opcion_ingresada == "B": # Movimientos (al azar)
    moneda_elegida = seleccionar_moneda()
    if confirma('imprimir') == "N":                 #Si no quiere imprimir puede ver los movimientos por pantalla
      print(f"Sus moviminetos en {moneda_elegida} son:")
      #if devolucion > 0:
      #  print(f"---> INGRESO $ {devolucion} por transferencia fallida") 
      for i in range(10):
        print(f"--->  {gastos[random.randint(0,9)]} : ${round(random.uniform(0.00, 9999.99),2)}")
    else:         #Si pide imprimir no vera los movimientos... se "simula" que se impime un tiket
      print("Su comprobante de Saldo se esta imprimiendo ...")
  else:
    print("opcion no valida")


def menu_opcion_2(saldo, moneda_elegida):
  saldo = retira_monto(saldo, moneda_elegida)
  if saldo != 0:
    if confirma('salir') == "N":        #El monto exede el saldo, ¿quiere salir?
      retira_monto(saldo, moneda_elegida)

  return saldo

# ------------------------------
def menu_opcion_3(saldo_pesos, saldo_soles, cuenta_ingresada):
  
  cuenta_ingresada = int (input ("Ingrese numero de cuenta: "))
  if seleccionar_moneda()=='Pesos': 
    saldo=saldo_pesos
  else:
    saldo=saldo_soles
    
  monto_transferencia = int(input("Ingrese monto a transferir: "))
  if monto_transferencia < saldo:
    saldo-= monto_transferencia
    if cuenta_ingresada != cuenta:
      print("La cuenta ingresada no existe")    
      #devolucion = monto_transferencia
      saldo+= monto_transferencia
      print(f"el monto {monto_transferencia} se devolvió su saldo es de {saldo}")
    if cuenta_ingresada == cuenta:
      print("Transferencia realizada con exito")
  else:
    print("Saldo insuficiente")
  

  return saldo

# -------------------------------------------------------------------
# Main
#
if solicitar_clave() and solicitar_dni():

  while opcion_menu_principal!=4:
    # ------------------------------
    # Menu Principal
    #
    opcion_menu_principal = int(input(mensaje_menu_principal))
    # ------------------------------
    # Ejecuto el Menu de la Opcion 1
    if opcion_menu_principal==1:
      menu_opcion_1()
    # ------------------------------
    # Menu Opcion 2
    #
    if opcion_menu_principal==2:
      moneda_elegida = seleccionar_moneda()    #Pide el ingreso de la moneda
      if moneda_elegida=='Pesos':
        saldo=saldo_pesos
      else:
        saldo=saldo_soles

      saldo=menu_opcion_2(saldo, moneda_elegida)

      if moneda_elegida=='Pesos':
        saldo_pesos=saldo
      else:
        saldo_soles=saldo
    # ------------------------------              
    # Menu Opcion 3
    #
    if opcion_menu_principal==3:
      saldo=menu_opcion_3(saldo_pesos, saldo_soles, cuenta_ingresada, devolucion)
      if moneda_elegida=='Pesos':
        saldo_pesos=saldo
        #devolucion_pesos= devolucion
      else:
        saldo_soles=saldo 
        #devolucion_soles= devolucion
else:
  print("Tarjeta retenida por exeso de reintentos de clave invalida")
    # ------------------------------              
    # Cuenta regresiva
    # no es necesario pero me parecio piola
    #import time 
    #while regresiva > 0: 
    #  print (f'Retire su tarjeta en {regresiva}') 
    #  regresiva-=1
    #  time.sleep(1)
    #print("ups! el cajero se comio tu tarjeta \nla proxima hay que ser mas rapidos :)")


    
