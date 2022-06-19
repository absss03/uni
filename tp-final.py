
import random
import time 

clave=1234
clave_ingresada=0
dni = 12345678
dni_ingresado = 0
cuenta = 98765
cuenta_ingresada = 0

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
devolucion= 0
devolucion_pesos=0
devolucion_soles=0
regresiva = 10

def prsiona_boton():
  x=not input('presiona el boton de activación para continuar... \n>')
  while x==False:
    print("tecla incorrecta")
    x=not input('presiona enter para continuar...')
  else: 
    x=True

  return x
# ------------------------------
def selecciona_moneda():
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
def solicita_clave():
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
def solicita_dni():
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
  error=0
  monto_a_retirar = int(input("Ingrese monto a retirar: "))     #Pide el monto a retirar
  if monto_a_retirar <= saldo:
    if solicita_clave():
      saldo-=monto_a_retirar
      if confirma('imprimir') == "N":
        print("Transaccion realizada con exito")
      else:
        print("Su comprobante de Saldo se esta imprimiendo ...")
    else:
     error=1
  else:
    print(f"el monto {monto_a_retirar} a retirar en {moneda_elegida} exede el saldo: {saldo}")
    error=1
  
  return saldo, error
# ------------------------------
def menu_opcion_1(saldo_pesos, saldo_soles):
  opcion_ingresada=input(mensaje_menu_opcion_1)

  if opcion_ingresada == "A": # Posicion Global o Saldo
    moneda_elegida = selecciona_moneda()
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
    moneda_elegida = selecciona_moneda()
    if confirma('imprimir') == "N":                 #Si no quiere imprimir puede ver los movimientos por pantalla
      print(f"Sus moviminetos en {moneda_elegida} son:")
      if devolucion > 0:
        if moneda_elegida== 'Pesos':
          print(f"---> INGRESO $ {devolucion_pesos} por transferencia fallida")
          saldo_pesos += devolucion_pesos   #Aca devuelve la plata porque no puedo hacer que pasen 3 dias
        else:
          print(f"---> INGRESO $ {devolucion_soles} por transferencia fallida")
          saldo_soles += devolucion_soles
      for i in range(10):
        print(f"--->  {gastos[random.randint(0,9)]} : ${round(random.uniform(0.00, 9999.99),2)}")
    else:         #Si pide imprimir no vera los movimientos... se "simula" que se impime un tiket
      print("Su comprobante de Saldo se esta imprimiendo ...")
  else:
    print("opcion no valida")

  return saldo_pesos, saldo_soles  #Necesito que retorne esto para poder actualizar el valor de las variables
# ------------------------------
def menu_opcion_2(saldo, moneda_elegida):
  saldo, error = retira_monto(saldo, moneda_elegida)
  if error != 0:   #Si se cumple es o porque el monto exede el saldo o porque la contraseña es incorrecta
    if confirma('salir') == "N":        #El monto exede el saldo, ¿quiere salir?
      retira_monto(saldo, moneda_elegida)

  return saldo
# ------------------------------
def menu_opcion_3(saldo_pesos, saldo_soles, cuenta_ingresada):
  devolucion = 0
  cuenta_ingresada = int (input ("Ingrese numero de cuenta: "))
  moneda_elegida=selecciona_moneda()
  if moneda_elegida=='Pesos': 
    saldo=saldo_pesos
  else:
    saldo=saldo_soles
    
  monto_transferencia = int(input("Ingrese monto a transferir: "))
  if monto_transferencia < saldo:
    saldo-= monto_transferencia
    if cuenta_ingresada != cuenta:
      print("La cuenta ingresada no existe")    
      devolucion = monto_transferencia
      print(f"el monto {monto_transferencia} se devolverá su saldo es de {saldo}")
    if cuenta_ingresada == cuenta:
      print("Transferencia realizada con exito")
  else:
    print("Saldo insuficiente")
  

  return saldo, devolucion, moneda_elegida

if prsiona_boton():
  print('._______________________.  \n|                       |   \n| BIENVENIDO AL CAJERO  |   \n| AUTOMATICO INTERBANCA | \n|_______________________|')
# -------------------------------------------------------------------
# Main
#
if solicita_clave() and solicita_dni():

  while opcion_menu_principal!=4:
    # ------------------------------
    # Menu Principal
    #
    opcion_menu_principal = int(input(mensaje_menu_principal))
    # ------------------------------
    # Ejecuto el Menu de la Opcion 1
    if opcion_menu_principal==1:
      saldo_pesos, saldo_soles=menu_opcion_1(saldo_pesos, saldo_soles)  #Esto me permite actualizar el valor de las variable, es decir agregarle la devolucion al saldo
    # ------------------------------
    # Menu Opcion 2
    #
    if opcion_menu_principal==2:
      moneda_elegida = selecciona_moneda()    #Pide el ingreso de la moneda
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
      saldo, devolucion, moneda_elegida=menu_opcion_3(saldo_pesos, saldo_soles, cuenta_ingresada)
      if moneda_elegida=='Pesos':
        saldo_pesos=saldo
        devolucion_pesos= devolucion
      else:
        saldo_soles=saldo 
        devolucion_soles= devolucion
    # ------------------------------              
    # Cuenta regresiva
    # no es necesario pero me parecio piola
    
  while regresiva > 0: 
    print (f'Retire su tarjeta en {regresiva}') 
    regresiva-=1
    time.sleep(1)
  print("ups! el cajero se comio tu tarjeta \nla proxima hay que ser mas rapidos :)")
else:
  print("Tarjeta retenida por exeso de reintentos de clave invalida")


    
