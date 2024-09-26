from flask import Flask, request, render_template, url_for, redirect
import random

app = Flask(__name__)
    
# @app.route("/")
# def index():
#     return render_template('index.html')
# Función para mostrar el mensaje de bienvenida y el menú principal
@app.route("/dialogo")
def mensaje_bienvenida():
    print("\n--- ¡Bienvenido al Hotel Paradice! ---")
    print("1. Realizar o modificar su reservación")
    print("2. Check-in y Check-out")
    print("3. Servicios Incluidos")
    print("4. Servicios Adicionales")
    print("5. Métodos de Pago")
    print("6. Atención al Cliente")
    print("7. Preguntas frecuentes")
    return input("\nSelecciona una opción: ")

# Función para el submenú de reservaciones
def menu_reservaciones():
    print("\n--- Menú de Reservaciones ---")
    print("1. Realizar una reservación")
    print("2. Verificar una reservación")
    print("3. Modificar una reservación")
    print("4. Cancelar una reservación")
    return input("\nSelecciona una opción de reservación: ")

# Submenú para realizar una nueva reservación
import re
from datetime import datetime

def solicitar_entrada(mensaje, patron, mensaje_error, longitud_minima=0):
    while True:
        entrada = input(mensaje)
        if len(entrada) >= longitud_minima and re.match(patron, entrada):
            return entrada
        else:
            print(mensaje_error)

def validar_fecha(fecha_texto):
    return datetime.strptime(fecha_texto, "%d/%m/%Y")

def realizar_reservacion():
    # Validación del nombre (solo letras y espacios, mínimo 8 caracteres)
    nombre = solicitar_entrada(
        "Por favor, ingrese su nombre completo (mínimo 8 caracteres, solo letras): ",
        r"^[A-Za-z\s]+$",
        "Entrada inválida. El nombre solo debe contener letras y espacios, y tener al menos 16 caracteres.",
        longitud_minima=8
    )

    print(f"\nGracias, {nombre}. Ahora ingrese las fechas de su reservación.")

    # Validación de la fecha de entrada (DD/MM/AAAA)
    while True:
        fecha_entrada_texto = solicitar_entrada(
            "Fecha de entrada (DD/MM/AAAA): ",
            r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([0-9]{4})$",
            "Entrada inválida. La fecha debe tener el formato DD/MM/AAAA."
        )
        fecha_entrada = validar_fecha(fecha_entrada_texto)
        break

    # Validación de la fecha de salida (DD/MM/AAAA) y que sea mayor que la de entrada
    while True:
        fecha_salida_texto = solicitar_entrada(
            "Fecha de salida (DD/MM/AAAA): ",
            r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([0-9]{4})$",
            "Entrada inválida. La fecha debe tener el formato DD/MM/AAAA."
        )
        fecha_salida = validar_fecha(fecha_salida_texto)
        if fecha_salida > fecha_entrada:
            break
        else:
            print("La fecha de salida debe ser posterior a la fecha de entrada.")

    print(f"\nFechas ingresadas: Entrada - {fecha_entrada_texto}, Salida - {fecha_salida_texto}")

    # Aquí debes definir tu función seleccionar_habitacion
    return seleccionar_habitacion(nombre, fecha_entrada_texto, fecha_salida_texto)


# Función para seleccionar el tipo de habitación y mostrar servicios incluidos
def seleccionar_habitacion(nombre, fecha_entrada, fecha_salida):
    print("\n--- Seleccione el tipo de habitación ---")
    print("1. Habitación Estándar")
    print("2. Suite")
    print("3. Habitación Familiar")
    tipo_habitacion = input("\nSelecciona una opción: ")

    if tipo_habitacion == "1":
        habitacion = "Habitación Estándar"
        print("\n--- Servicios Incluidos para Habitación Estándar ---")
        print("- Wi-Fi gratuito\n- Desayuno continental\n- Acceso a la piscina\n- Televisión por cable")
    elif tipo_habitacion == "2":
        habitacion = "Suite"
        print("\n--- Servicios Incluidos para Suite ---")
        print("- Wi-Fi gratuito\n- Desayuno buffet\n- Acceso a la piscina y gimnasio\n- Televisión por cable y Netflix\n- Minibar\n- Servicio a la habitación 24 horas")
    elif tipo_habitacion == "3":
        habitacion = "Habitación Familiar"
        print("\n--- Servicios Incluidos para Habitación Familiar ---")
        print("- Wi-Fi gratuito\n- Desayuno para 4 personas\n- Acceso a la piscina y gimnasio\n- Televisión por cable\n- Zona de juegos para niños\n- Servicio de niñera bajo solicitud")
    else:
        print("Opción inválida.")
        return

    confirmar_reservacion(nombre, fecha_entrada, fecha_salida, habitacion)

# Confirmar reservación y preguntar por servicios adicionales
def confirmar_reservacion(nombre, fecha_entrada, fecha_salida, habitacion):
    print(f"\n--- Confirmación de Reservación ---")
    print(f"Nombre: {nombre}")
    print(f"Fecha de entrada: {fecha_entrada}")
    print(f"Fecha de salida: {fecha_salida}")
    print(f"Habitación seleccionada: {habitacion}")

    confirmacion = input("\n¿Desea continuar con la reservación? (1 para Sí, 0 para No): ")

    if confirmacion == "1":
        servicios_adicionales(nombre, fecha_entrada, fecha_salida, habitacion)
    else:
        print("\nReservación cancelada. Volviendo al menú principal...")

# Función para seleccionar servicios adicionales
def servicios_adicionales(nombre, fecha_entrada, fecha_salida, habitacion):
    print("\n¿Desea agregar servicios adicionales a su reservación?")
    print("1. Sí")
    print("2. No")
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        print("\n--- Servicios Adicionales ---")
        print("1. Spa")
        print("2. Transporte")
        print("3. Cenas")
        print("4. No agregar servicios adicionales")
        servicio_seleccionado = input("\nSeleccione el servicio adicional: ")

        if servicio_seleccionado in ["1", "2", "3"]:
            servicio = ["Spa", "Transporte", "Cenas"][int(servicio_seleccionado) - 1]
            print(f"\nServicio adicional seleccionado: {servicio}")
            confirmar_pago(nombre, fecha_entrada, fecha_salida, habitacion, servicio)
        elif servicio_seleccionado == "4":
            confirmar_pago(nombre, fecha_entrada, fecha_salida, habitacion, None)
        else:
            print("Opción inválida.")
            servicios_adicionales(nombre, fecha_entrada, fecha_salida, habitacion)
    elif opcion == "2":
        confirmar_pago(nombre, fecha_entrada, fecha_salida, habitacion, None)
    else:
        print("Opción inválida.")
        servicios_adicionales(nombre, fecha_entrada, fecha_salida, habitacion)

# Función para confirmar el pago y generar número de referencia
def confirmar_pago(nombre, fecha_entrada, fecha_salida, habitacion, servicio):
    print("\n--- Métodos de Pago ---")
    print("1. PSE")
    print("2. Nequi")
    print("3. Daviplata")
    print("4. Tarjeta de crédito")
    metodo_pago = input("\nSeleccione su método de pago: ")

    # Generar número de referencia de la reservación
    numero_referencia = random.randint(100000, 999999)

    # Confirmación final de la reservación
    print(f"\n¡Reservación confirmada! Número de referencia: {numero_referencia}")
    print(f"Nombre: {nombre}\nFecha de entrada: {fecha_entrada}\nFecha de salida: {fecha_salida}\nHabitación: {habitacion}")
    if servicio:
        print(f"Servicio adicional: {servicio}")
    print(f"Método de pago: {['PSE', 'Nequi', 'Daviplata', 'Tarjeta de crédito'][int(metodo_pago)-1]}")
    print(f"\nPuedes usar tu número de referencia para verificar o modificar tu reservación.")

# Función para verificar una reservación
def verificar_reservacion():
    referencia = input("Por favor, ingrese su número de referencia: ")
    print(f"\nVerificando reservación con número de referencia: {referencia}...")
    print("Reservación encontrada. Aquí están los detalles de tu reservación.")

# Función para modificar una reservación
def modificar_reservacion():
    referencia = input("Por favor, ingrese su número de referencia: ")
    print(f"\nModificando reservación con número de referencia: {referencia}...")

# Función para cancelar una reservación
def cancelar_reservacion():
    referencia = input("Por favor, ingrese su número de referencia: ")
    print(f"\nCancelando reservación con número de referencia: {referencia}...")
    numero_cancelacion = random.randint(100000, 999999)
    print(f"Reservación cancelada exitosamente. Número de cancelación: {numero_cancelacion}")

# Submenú de Check-in y Check-out
def menu_check_in_out():
    print("\n--- Menú de Check-in y Check-out ---")
    print("1. Ver horario de Check-in y Check-out")
    print("2. Solicitar Check-in temprano")
    print("3. Solicitar Check-out tardío")
    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        print("\nHorario de Check-in: 3:00 p.m. del día de llegada")
        print("Horario de Check-out: 12:00 p.m. del día de salida")
    elif opcion == "2":
        print("\nCheck-in temprano disponible de 6:00 a.m. a 11:00 a.m. (Sujeto a disponibilidad)")
    elif opcion == "3":
        print("\nCheck-out tardío disponible de 4:00 p.m. a 9:00 p.m. (Sujeto a disponibilidad)")
    else:
        print("Opción inválida.")

# Submenú de Servicios Incluidos
def menu_servicios_incluidos():
    print("\n--- Menú de Servicios Incluidos ---")
    print("1. Ver servicios incluidos en mi reservación")
    print("2. Información sobre el desayuno")
    print("3. Acceso a Wi-Fi, gimnasio y piscina")
    return input("\nSelecciona una opción: ")

# Función para ver servicios incluidos según el tipo de habitación
def ver_servicios_incluidos():
    print("\n--- Servicios Incluidos por Habitación ---")
    print("1. Habitación Estándar")
    print("2. Suite")
    print("3. Habitación Familiar")
    tipo_habitacion = input("\nSelecciona una opción: ")

    if tipo_habitacion == "1":
        print("\n--- Servicios Incluidos para Habitación Estándar ---")
        print("- Wi-Fi gratuito\n- Desayuno continental\n- Acceso a la piscina\n- Televisión por cable")
    elif tipo_habitacion == "2":
        print("\n--- Servicios Incluidos para Suite ---")
        print("- Wi-Fi gratuito\n- Desayuno buffet\n- Acceso a la piscina y gimnasio\n- Televisión por cable y Netflix\n- Minibar\n- Servicio a la habitación 24 horas")
    elif tipo_habitacion == "3":
        print("\n--- Servicios Incluidos para Habitación Familiar ---")
        print("- Wi-Fi gratuito\n- Desayuno para 4 personas\n- Acceso a la piscina y gimnasio\n- Televisión por cable\n- Zona de juegos para niños\n- Servicio de niñera bajo solicitud")
    else:
        print("Opción inválida.")

# Función para mostrar la información sobre el desayuno
def informacion_desayuno():
    print("\n--- Información sobre el Desayuno ---")
    print("1. Habitación Estándar:")
    print("- Desayuno Continental de 7:00 a.m. a 10:00 a.m. en el Restaurante Principal.")
    print("- Incluye: Panes, croissants, tostadas, mermeladas, jugo de naranja, café, frutas y yogur.")

    print("\n2. Suite:")
    print("- Desayuno Buffet de 7:00 a.m. a 11:00 a.m. en el Restaurante Exclusivo para Suites.")
    print("- Incluye: Panes frescos, quesos, huevos al gusto, pancakes, frutas frescas, jugos naturales, yogures y smoothies.")

    print("\n3. Habitación Familiar:")
    print("- Desayuno Buffet Familiar de 7:00 a.m. a 11:00 a.m. en el Área Familiar del Restaurante.")
    print("- Incluye: Pancakes, waffles, jugos, yogur, opciones sin lactosa, galletas, muffins para niños.")

    input("\nPresiona Enter para volver al menú principal.")

# Función para mostrar información sobre acceso a Wi-Fi, gimnasio y piscina
def acceso_wifi_gimnasio_piscina():
    print("\n--- Acceso a Wi-Fi, Gimnasio y Piscina ---")
    print("Wi-Fi:")
    print("- Wi-Fi gratuito en todo el hotel (habitaciones, áreas comunes, sala de reuniones).")
    print("- Soporte técnico disponible 24 horas.")

    print("\nGimnasio:")
    print("- Horario: 6:00 a.m. a 10:00 p.m.")
    print("- Equipos: Cardio, pesas, yoga, clases grupales.")

    print("\nPiscina:")
    print("- Horario: 7:00 a.m. a 9:00 p.m.")
    print("- Piscina principal climatizada, jacuzzi, piscina infantil.")

    input("\nPresiona Enter para volver al menú principal.")

# Submenú de Servicios Adicionales: Cena romántica, transporte, etc.
def menu_servicios_adicionales():
    print("\n--- Servicios Adicionales ---")
    print("1. Spa")
    print("2. Transporte desde/hacia el aeropuerto")
    print("3. Cena Romántica")
    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        print("\nReservando acceso al Spa...")
    elif opcion == "2":
        print("\nSolicitando transporte desde/hacia el aeropuerto...")
        print("Abriendo link para Uber o Taxi...")
    elif opcion == "3":
        menu_cena_romantica()
    else:
        print("Opción inválida.")

# Submenú para reservar una cena romántica
def menu_cena_romantica():
    print("\n--- Cena Romántica ---")
    print("1. Cena Romántica Privada: Terraza privada, cena de 3 platos, vino espumoso.")
    print("2. Experiencia de Spa y Cena Romántica: Masaje en pareja y cena en restaurante.")
    print("3. Cena Romántica en la Playa: Cena en la playa bajo las estrellas.")
    print("4. Cena Romántica en el Balcón: Cena privada en el balcón de tu habitación.")

    opcion_cena = input("\nSelecciona una opción de cena romántica: ")
    if opcion_cena in ["1", "2", "3", "4"]:
        print(f"\nCena seleccionada. Procediendo con la reservación...")
        confirmar_pago_cena()
    else:
        print("Opción inválida.")

# Función para confirmar el pago de la cena romántica
def confirmar_pago_cena():
    print("\n--- Métodos de Pago para la Cena Romántica ---")
    print("1. PSE")
    print("2. Nequi")
    print("3. Daviplata")
    print("4. Tarjeta de crédito")
    metodo_pago = input("\nSeleccione su método de pago: ")
    print(f"\nPago confirmado con {['PSE', 'Nequi', 'Daviplata', 'Tarjeta de crédito'][int(metodo_pago)-1]}. ¡Disfruta de tu cena romántica!")

# Submenú de atención al cliente
def menu_atencion_cliente():
    print("\n--- Atención al Cliente ---")
    print("1. Número de teléfono para asesoría personalizada")
    print("2. Redes sociales del hotel")
    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        print("\nNúmero de teléfono para asesoría personalizada: 3006568642")
    elif opcion == "2":
        print("\nRedes sociales del Hotel XYZ:")
        print("- Facebook: facebook.com/HotelXYZ")
        print("- Instagram: instagram.com/HotelXYZ")
        print("- X (Twitter): twitter.com/HotelXYZ")
    else:
        print("Opción inválida.")

# Submenú de preguntas frecuentes
def menu_preguntas_frecuentes():
    print("\n--- Preguntas Frecuentes ---")
    print("1. ¿Cómo puedo hacer una reserva?")
    print("2. ¿Cuál es la política de cancelación?")
    print("3. ¿Qué tipos de habitaciones están disponibles?")
    print("4. ¿A qué hora puedo hacer el check-in?")
    print("5. ¿Cuál es la hora de salida?")
    print("6. ¿Es posible hacer un check-in temprano o un check-out tardío?")
    print("7. ¿El hotel ofrece servicio de Wi-Fi?")
    print("8. ¿El hotel tiene estacionamiento?")
    return input("\nSelecciona una pregunta para ver la respuesta: ")

# Función para responder preguntas frecuentes
def responder_pregunta_frecuente(pregunta):
    respuestas = {
        "1": "Puedes hacer una reserva directamente en nuestra página web o contactarnos por teléfono.",
        "2": "Puedes cancelar tu reserva hasta 48 horas antes sin costo. Después de ese tiempo, se aplicará un cargo.",
        "3": "Ofrecemos habitaciones sencillas, dobles y familiares.",
        "4": "El check-in está disponible a partir de las 3:00 PM.",
        "5": "La hora de salida es a las 12:00 PM.",
        "6": "Esto depende de la disponibilidad. Consulta directamente con el hotel.",
        "7": "Sí, contamos con Wi-Fi gratuito en todas las áreas del hotel.",
        "8": "Sí, tenemos estacionamiento gratuito para nuestros huéspedes."
    }
    print(f"\nRespuesta: {respuestas.get(pregunta, 'Opción inválida.')}")

# Función principal para ejecutar el chatbot
def main():
    while True:
        opcion = mensaje_bienvenida()

        if opcion == "1":
            sub_opcion = menu_reservaciones()
            if sub_opcion == "1":
                realizar_reservacion()
            elif sub_opcion == "2":
                verificar_reservacion()
            elif sub_opcion == "3":
                modificar_reservacion()
            elif sub_opcion == "4":
                cancelar_reservacion()
            else:
                print("Opción inválida.")

        elif opcion == "2":
            menu_check_in_out()

        elif opcion == "3":
            sub_opcion_servicios = menu_servicios_incluidos()
            if sub_opcion_servicios == "1":
                ver_servicios_incluidos()
            elif sub_opcion_servicios == "2":
                informacion_desayuno()
            elif sub_opcion_servicios == "3":
                acceso_wifi_gimnasio_piscina()
            else:
                print("Opción inválida.")

        elif opcion == "4":
            menu_servicios_adicionales()

        elif opcion == "5":
            print("\nMostrando métodos de pago...")

        elif opcion == "6":
            menu_atencion_cliente()

        elif opcion == "7":
            pregunta = menu_preguntas_frecuentes()
            responder_pregunta_frecuente(pregunta)

        else:
            print("Opción inválida. Por favor, selecciona nuevamente.")

if(__name__=='__main__'):
     app.run(debug=True)
