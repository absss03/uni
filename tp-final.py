
import random
import time 

clave=1234
dni = 12345678
cuenta = 98765


opcion_menu_principal=0
mensaje_menu_principal = "\n--------------- \n1. Consultas \n2. Retiros \n3. Transferencias \n4. Salir \n--------------- \nelija opcion >> "
mensaje_menu_opcion_1 = "\n--------------- \nA - Posicion Global \nB - Movimientos \n--------------- \neliga opcion >> "
mensaje_menu_opcion_3 = "\n--------------- \nA - Indique numero de cuenta destino \nB - volver  \n--------------- \nelija opcion >> "

gastos=['INGRESO - DEPOSITO','EGRESO - SUPERMERCADO','EGRESO - CARNICERIA','EGRESO - EXTRACCION','EGRESO - RESTAURANTE','EGRESO - ZAPATERIA','EGRESO - TRANSFERENCIA','EGRESO - MASCOTERIA','INGRESO - TRANSFERENCIA','EGRESO - FARMACIA']
tipo_de_moneda= "-------------\nA.Pesos\nB.Soles\n------------ \nSeleccione el tipo de moneda>> "

saldo_pesos = 85000
saldo_soles = 3564

devolucion= 0
devolucion_pesos=0
devolucion_soles=0
regresiva = 10

def prsiona_boton():
    ''' 
    Esta funcion confirma que se haya presionado la tecla enter.
    '''
    x=not input('presiona el boton de activación para continuar... \n>')
    while x==False:
        print("tecla incorrecta")
        x=not input('presiona enter para continuar...')
    else: 
        x=True

    return x
# ------------------------------
def selecciona_moneda():
    ''' 
    Esta funcion le permite al usuario elegir entre Soles y Pesos y devuelve su eleccion.
    '''
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
    '''
    Esta funcion sirve para mostrar un mensaje que se reponde con si o no y devuelve la eleccion del usuario.
    '''
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
    '''
    Esta funcion solicita el ingreso de una clave y la compara con la clave en la "base de datos". 
    Si no coinciden le permite al usuario hasta tres intentos.
    '''
    clave_aceptada=False
    reintentos=0

    while reintentos<3 and not clave_aceptada:
        clave_ingresada= int(input("ingrese su clave: "))     
        if clave_ingresada != clave:         #si la clave no es correcta
            print(f"La clave ingresada {clave_ingresada}, no es valida")
            reintentos+=1
        else:
            clave_aceptada=True

    return clave_aceptada
# ------------------------------
def solicita_dni():
    '''
    Esta funcion solicita el ingreso de de un dni hasta que el mismo coincida con el que se encuentra en la "base de datos".
    '''
    dni_aceptado=False

    while not dni_aceptado:         #si lel dni no es correcto
        dni_ingresado = int(input("ingrese su dni: "))
        if dni_ingresado != dni:
            print(f"El nro de DNI ingresado {dni_ingresado}, no es valido")
        else:
            dni_aceptado=True

    return dni_aceptado
# ------------------------------
def retira_monto(saldo_temp):
    '''
    Esta funcion verifica que el monto a retirar sea menor que el saldo.
    Si es asi, retira la cantidad especificada por el usuario, de lo contrario le informara que la la transaccion no podra realizarse.
    Ademas si el retiro es efectivo le ofrece al usuario la posibilidad de imprimir o ver por pantalla el comprobate. 
    (Si elige la primer opcion solo vera un mensaje en la terminal, ya que la impresion de un tiket es simulada).
    '''
    error=0
    monto_a_retirar = int(input("Ingrese monto a retirar: "))         #Pide el monto a retirar
    if monto_a_retirar <= saldo_temp:
        if solicita_clave():
            saldo_temp-=monto_a_retirar
            if confirma('imprimir') == "N":
                print("Transaccion realizada con exito")
            else:
                print("Su comprobante de Saldo se esta imprimiendo ...")
        else:
            error=1
    else:
        print(f"el monto {monto_a_retirar} a retirar en {moneda_elegida} exede el saldo: {saldo}")
        error=1
    
    return saldo_temp, error
# ------------------------------
def menu_opcion_1(saldo_pesos_temp, saldo_soles_temp):
    '''
    Esta funcion se encarga de mostrar las dos opciones que se encuentran en el Menu 1 (Posicion global o Movimientos).
    Ademas dentro de los Movimientos podra verse la devolucion del dinero cuando se realiza una transferencia a una cuenta que no existe.
    Del mismo modo que en etras funciones, cuando el usuario elige la imprsion de un comprobante solo vera un mensaje en la terminal ya que la misma es simulada.
    '''
    opcion_ingresada=input(mensaje_menu_opcion_1)

    if opcion_ingresada == "A": # Posicion Global o Saldo
        moneda_elegida_temp = selecciona_moneda()
        if moneda_elegida_temp=='Pesos':
            if confirma('imprimir') == "N":
                print(f"Su saldo disponible en {moneda_elegida_temp} es de: ${saldo_pesos_temp}")
            else:
                print("Su comprobante de Saldo se esta imprimiendo ...")
        elif moneda_elegida_temp =='Soles':
            if confirma('imprimir') == "N":
                print(f"Su saldo disponible en {moneda_elegida_temp} es de: ${saldo_soles_temp}")
            else:
                print("Su comprobante de Saldo se esta imprimiendo ...")

    elif opcion_ingresada == "B": # Movimientos (al azar)
        moneda_elegida_temp = selecciona_moneda()
        if confirma('imprimir') == "N":                                 #Si no quiere imprimir puede ver los movimientos por pantalla
            print(f"Sus moviminetos en {moneda_elegida_temp} son:")
            if devolucion > 0:
                if moneda_elegida_temp == 'Pesos':
                    print(f"---> INGRESO $ {devolucion_pesos} por transferencia fallida")
                    saldo_pesos_temp += devolucion_pesos     #Aca devuelve la plata porque no puedo hacer que pasen 3 dias
                else:
                    print(f"---> INGRESO $ {devolucion_soles} por transferencia fallida")
                    saldo_soles_temp += devolucion_soles
            for i in range(10):
                print(f"--->    {gastos[random.randint(0,9)]} : ${round(random.uniform(0.00, 9999.99),2)}")
        else:                 #Si pide imprimir no vera los movimientos... se "simula" que se impime un tiket
            print("Su comprobante de Saldo se esta imprimiendo ...")
    else:
        print("opcion no valida")

    return saldo_pesos_temp, saldo_soles_temp    #Necesito que retorne esto para poder actualizar el valor de las variables
# ------------------------------
def menu_opcion_2(saldo_temp):
    '''
    Esta funcion permite realizar retiros de dinero unicamente si el monto a retirar es menor o igual al saldo.
    Si este se exede el usuario tendra la opcion de elegir entre cambiar dicho monto una vez mas o salir del Menu 2.
    '''
    saldo_temp, error = retira_monto(saldo_temp)
    if error != 0:     #Si se cumple es o porque el monto exede el saldo o porque la contraseña es incorrecta
        if confirma('salir') == "N":                #El monto exede el saldo, ¿quiere salir?
            retira_monto(saldo_temp)

    return saldo_temp
# ------------------------------
def menu_opcion_3(saldo_pesos_temp, saldo_soles_temp):
    '''
    Esta funcion permite realizar transferencias a cualquier cuenta.
    La misma sera verificada luego de ingresar el monto a transferir y si no coincide con la cuenta que esta en la "base de datos"
    le devolvera el dinero al usuario. (Esto se podra ver en el menu 1 opcion B)
    '''
    devolucion_temp = 0
    cuenta_ingresada = int (input ("Ingrese numero de cuenta: "))
    moneda_elegida_temp =selecciona_moneda()
    if moneda_elegida_temp =='Pesos': 
        saldo_temp=saldo_pesos_temp
    else:
        saldo_temp=saldo_soles_temp
        
    monto_transferencia = int(input("Ingrese monto a transferir: "))
    if monto_transferencia < saldo_temp:
        saldo_temp-= monto_transferencia
        if cuenta_ingresada != cuenta:
            print("La cuenta ingresada no existe")        
            devolucion_temp = monto_transferencia
            print(f"el monto {monto_transferencia} se devolverá su saldo es de {saldo_temp}")
        if cuenta_ingresada == cuenta:
            print("Transferencia realizada con exito")
    else:
        print("Saldo insuficiente")
    

    return saldo_temp, devolucion_temp, moneda_elegida_temp

if prsiona_boton():
    print('._______________________.  \n|                     |   \n| BIENVENIDO AL CAJERO  |   \n| AUTOMATICO INTERBANCA | \n|_______________________|')
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
            saldo_pesos, saldo_soles=menu_opcion_1(saldo_pesos, saldo_soles)    #Esto me permite actualizar el valor de las variable, es decir agregarle la devolucion al saldo
        # ------------------------------
        # Menu Opcion 2
        #
        if opcion_menu_principal==2:
            moneda_elegida = selecciona_moneda()        #Pide el ingreso de la moneda
            if moneda_elegida=='Pesos':
                saldo=saldo_pesos
            else:
                saldo=saldo_soles

            saldo=menu_opcion_2(saldo)
            if moneda_elegida=='Pesos':
                saldo_pesos=saldo
            else:
                saldo_soles=saldo
        # ------------------------------                            
        # Menu Opcion 3
        #
        if opcion_menu_principal==3:
            saldo, devolucion, moneda_elegida=menu_opcion_3(saldo_pesos, saldo_soles)
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


        
