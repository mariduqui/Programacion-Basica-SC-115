#Datos personales que el usuario necesita ingresar. (Mariana 1era parte)

Nombre_completo= input("Ingrese su nombre completo: ")
Número_telefonico= input("Ingrese su número telefónico: ")
Correo_electrónico= input ("Ingrese su correo electrónico: ")

print("Muchas gracias por la información")

#Curso teórico

horasTeorico=""
diasTeorico=""

#Clases de manejo

horasClases=""
diasClases=""

#Menú de servicios (Propuesta de Meggan)

print ("Bienvenido al menú de sevicios ")

print ("1. Curso teórico")
print ("2. Clases de manejo")
print ("3. Dictamen médico")

# Bucle principal:

while True:
    #El usuario selecciona una opción
    opción = int(input("Seleccione una opción: "))

    #Opción 1: Servicio de Curso Teórico

    if opción ==1:

        print ("Ha seleccionado el servicio de curso teórico")
        print ("1. Seleccione cantidad de horas")
        print ("2. Sleccione dias de lunes a sabado de 8am - 9pm")
        print ("3. Volver al menú de servicios")

        #Bucle del servicio de Curso Teórico

        while True:
            sub_opcion = int(input("Seleccione una opción: "))

            if sub_opcion == 1:
                print ("Ha seleccionado la opcion 1 del servicio de curso teórico")
            elif sub_opcion == 2:
                print ("Ha selecionado la opcion 2 del servicio de curso teórico") 
            elif sub_opcion ==3:
                break      #se sale del bucle del servicio de curso teorico 
    
    #Opción 2: Clases de Manejo

    if opción == 2:

        print ("Ha seleccionado el servicio curso de manejo")
        print ("1. Horas a contratar")
        print ("2. Carro propio - 3000 colones por hora")
        print ("3. Carro proporcionado por la academia - 4000 colones por hora")
        print ("4. Elegir dias a asistir a clases entre martes - domingo 8am-5pm")
        print ("5. Volver al menú de servicios")

        #Bucle del servicio de clases de manejo

        while True:
            sub_opcion = int(input("Seleccione una opción: "))

            if sub_opcion == 1:
                print ("Ha seleccionado la opcion 1 del curso de manejo")
            elif sub_opcion == 2:
                print ("Ha seleccionado la opción 2 del curso de manejo")
            elif su_opcion == 3:
                print("Ha seleccionado la opción 3 del curso de manejo")
            elif sub_opcion == 4:
                print ("Ha selecionado la opción 4 del curso de manejo")
            elif sub_opcion == 5:
                break      #se sale del bucle del servicio de curso de manejo

    
    #Opción 3: Dictamen Médico (pendiente)