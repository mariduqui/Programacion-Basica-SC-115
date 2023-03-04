#Academia de manejo
#Se solicita a la persona, el usuario y la contraseña para accesar al sistema de citas.

print("Bienvenido a la academia de manejo.")
print("Por favor ingrese sus datos: \n")
nombredeusuario = ""
contrasena = ""

dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"]


while nombredeusuario != "admin" or contrasena != "1234":
    nombredeusuario= input("Usuario: ")
    contrasena= input("Contraseña: ")
    if nombredeusuario == "admin" and contrasena == "1234":
        print("Bienvenido.\n")
    else:
        print("Usuario o contraseña incorrectos, por favor intente de nuevo. \n")

#Se solicitan los datos personales del usuario

print("A continuación, ingrese sus datos personales: \n")
nombre=input("Ingrese su nombre: ")
telefono=input("Ingrese su número de teléfono: ")
correo=input("Ingrese su correo electrónico: ")

print("Muchas gracias por la información")

#Curso teórico

horasTeorico=0
diasTeorico=""

#Clases de manejo

horasClases=0
diasClases=""

#Menú de servicios (Propuesta de Meggan)

print ("Bienvenido al menú de sevicios\n1. Curso teórico\n2. Clases de manejo\n3. Dictamen médico")

# Bucle principal:

while True:
#El usuario selecciona una opción
    opción = int(input("Seleccione una opción: "))

    #Opción 1: Servicio de Curso Teórico

    if opción ==1:
        #Sub_menú Curso Teórico
        print ("Ha seleccionado el servicio de curso teórico\n1. Seleccione cantidad de horas\n2. Seleccione dias de Lunes a Sábado de 8:00 - 21:00\n3. Volver al menú de servicios")
        #Bucle del servicio de Curso Teórico

        while True:
            sub_opcion = int(input("Seleccione una opción: "))

            if sub_opcion == 1:
                print ("Ha seleccionado la opcion 1 del servicio de curso teórico")
                horasTeorico=int(input("Ingrese la cantidad de horas: ")) #Solicitamos la cantidad de horas
                # Cuando se acaben las horas

                while horasTeorico > 0:
                    print("Sus horas disponibles para programar son: ",horasTeorico)
                    print ("Seleccione dias de Lunes a Sábado de 8 - 21")
                    print ("1. Lunes\n2. Martes\n3. Miercóles\n4. Jueves\n5. Viernes\n6. Sábado")
                    diasTeorico=int(input("Seleccione el día en el cúal asistirá a las clases teoricas: "))
                    if diasTeorico>=1 and diasTeorico<=6:
                        horaInicio = int(input("Ingrese la hora de incio entre 8- 20: "))
                        horasFin = int(input("Ingrese la hora de fin entre 8 - 20: "))
                        if(horasFin > horaInicio):
                            horaUtilizadas = horasFin- horaInicio
                            if(horaUtilizadas> horasTeorico):
                                print("No cuentas con horas disponibles")
                            else:
                                horasTeorico-=horaUtilizadas
                                print("Has reservado ",dias[diasTeorico-1]," de ", horaInicio, " hasta ", horasFin)

                        else:
                            print("La hora de finalización debe ser mayor a la hora de inicio")
                    else:
                        print("Ingreso un días donde no ofrecemos servicios")
                break;
            elif sub_opcion == 2:
                print ("Ha selecionado la opcion 2 del servicio de curso teórico")
            elif sub_opcion ==3:
                break      #se sale del bucle del servicio de curso teorico

    #Opción 2: Clases de Manejo

    if opción == 2:
        #Sub_menú Clases de Manejo
        print ("Ha seleccionado el servicio curso de manejo\n1. Horas a contratar\n2. Elegir dias a asistir a clases entre martes - domingo 8am-5pm\n3. Método de Transporte \n4. Volver al menú de servicios")

        #Bucle del servicio de clases de manejo

        while True:
            sub_opcion = int(input("Seleccione una opción: "))

            if sub_opcion == 1:
                print ("Ha seleccionado la opcion 1 del servicio de curso de manejo")
                horasClases=int(input("Ingrese la cantidad de horas: ")) #Solicitamos la cantidad de horas
                # Cuando se acaben las horas
                while horasClases > 0:
                    print("Sus horas disponibles para programar son: ",horasClases)
                    print ("Seleccione dias de Martes a Domingo de 8:00 - 17:00")
                    print ("1. Martes\n2. Miércoles\n3. Jueves\n4. Viernes\n5. Sábado\n6. Domingo")
                    diasClases=int(input("Seleccione el día en el cúal asistirá a las clases de manejo: "))
                    if diasClases>=1 and diasClases<=6:
                        horaInicio = int(input("Ingrese la hora de incio entre 8 - 17: "))
                        horasFin = int(input("Ingrese la hora de fin entre 8 - 17: "))
                        if(horasFin > horaInicio):
                            horaUtilizadas = horasFin- horaInicio
                            if(horaUtilizadas> horasClases):
                                print("No cuentas con horas disponibles")
                            else:
                                horasClases-=horaUtilizadas
                                print("Has reservado ",dias[diasClases-1]," de ", horaInicio, " hasta ", horasFin)

                        else:
                            print("La hora de finalización debe ser mayor a la hora de inicio")
                    else:
                        print("Ingreso un días donde no ofrecemos servicios")
                        
            if sub_opcion == 3:
                 print ("Ha seleccionado la opcion 3 del servicio de curso de manejo")
                 print ("Cuenta con vehículo propio? \n1. Sí\n2. No")
                 metodoTransporte=int(input("Seleccione una opción: "))
                 print("Ha seleccionado la" ,metodoTransporte)
                 break      #se sale del bucle del servicio de clases de manejo
                    

    #Opción 3: Dictamen Médico (pendiente)

    if opción == 3:
        print ("Ha seleccionado el servicio de dictamen médico")
        #Solicitamos datos
        tipoDeSangre=input("Ingrese su tipo de sangre: ")
        peso=int(input("Ingrese su peso: "))
        estatura=int(input("Ingrese su estatura: "))

        print ("¿Desea ser donador?\n1. Sí\n2. No")

        donador=int(input("Seleccione una opción: "))

            #Imprimimos la infomación
        if donador == 1:
            print ("Nombre",nombre,"\nTeléfono:",telefono,"\nEmail:",correo,"\nTipo de Sangre:",tipoDeSangre,"\nPeso:",peso,"\nEstatura:",estatura,"\nDonador?: Sí")
        else:
            print ("Nombre",nombre,"\nTeléfono:",telefono,"\nEmail:",correo,"\nTipo de Sangre:",tipoDeSangre,"\nPeso:",peso,"\nEstatura:",estatura,"\nDonador?: No")
