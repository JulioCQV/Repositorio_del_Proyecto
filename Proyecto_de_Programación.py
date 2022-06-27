#----------Proyecto de Programación----------
#Julio César
#Jordy Castrillo
#Wayath Vargas

#Variables
saldo=1000
respuesta=0
ingreso=0
retiro=0
#listas
registro_ingreso=[]
registro_retiro=[]

#---Verificar errores---
while True:
    try:

#----Menú Principal----
        while respuesta!=4:
            print( )
            print(
"""
+======================================================+
|          ¡Bienvenido al Banco Humildad!              |
|           ¿Que acción quieres realizar?              |
|                                                      |
|-Presione 1 para ingresar dinero                      |
|-Presione 2 para retirar dinero                       |
|-Presione 3 para mostrar su registro de actividad     |
|-Presione 4 para salir                                |
|                                                      |
| *Recuerda que nuestro banco solo trabaja con dolares*|
+======================================================+
Tu saldo es de""",saldo,"""dolares""")
            print()

#----Respuesta del usuario----
            respuesta= int(input(">>>"))

#----ingreso de dinero por parte del usuario------
            if respuesta==1:
                ingreso=float(input("¿Cuanto dinero quieres ingresar?>>"))

                if ingreso<=9:
                    print("-Lo sentimos, no puedes ingresar menos de 10 dolares-")

                elif ingreso>=100000:
                    print("-Lo sentimos, no puedes ingresar más de 100 000 dolares en una sola transacción, intentelo de nuevo-")

                elif ingreso>=10 and ingreso<=100000:
                    saldo+=ingreso

                #En esta lista se guardan los ingresos del cliente
                    registro_ingreso.append(ingreso)
                    
                #Aqui imprime el saldo
                    print("Su saldo es de:",saldo,"dolares")
                else:
                    quit

#----Retiro de dinero por parte del usuario-------
            elif respuesta==2:
                retiro=float(input("¿cuanto dinero quiere retirar?>>"))

                if saldo-retiro <0:
                    print()
                    print("Querido usuario, no tienes suficiente dinero, tu saldo es solo de",saldo,"dolares")

                elif retiro<1:
                    print("No puedes retirar cantidades negativas o cero")

                else:
                    saldo-=retiro

                #En esta lista se guardan los retiros del cliente
                    registro_retiro.append(retiro)

                #Aqui imprime el saldo
                    print("Tu saldo es de:",saldo,"dolares")

#----Registro de actividad----
            elif respuesta==3:
                print("Su historial de ingresos:",registro_ingreso)
                print()
                print("Su historial de retiros:",registro_retiro)

#----Salida-------
            elif respuesta==4:
                print("Muchas Gracias, que tengas un lindo día")
     
            else:
                print("Por favor, seleccione una opción correcta")

#----Control de errores-------
            break
    except ValueError:
        print ("Por favor, ingrese una opción valida")
        