from flask import Flask, request, render_template, url_for, jsonify
import re
from datetime import datetime
import random



import chatBot_ok as ch
import re

app = Flask(__name__)

chat_state = {
    "step": 0,
}

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/service")
def service():
    return render_template('service.html')


@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')



@app.route("/guide")
def guide():
    return render_template('guide.html')

@app.route("/package")
def package():
    return render_template('package.html')

@app.route("/single")
def single():
    return render_template('single.html')

@app.route("/testimonial")
def testimonial():
    return render_template('testimonial.html')




@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    # Lógica del chatbot    
    if chat_state["step"] == 0:
        response = "¿Cuál es su solicitud?\n1. Reservar\n2. Modificar reserva\n3. Cancelar reserva"
        chat_state["step"] = 1
    elif chat_state["step"] == 1:
        if user_message == "1":
            response = "Para reservar una habitación, ¿qué tipo desea?\n1. Sencilla\n2. Doble\n3. Suite"
            chat_state["step"] = 2
        elif user_message == "2":
            response = "Para modificar una reserva, por favor proporciona el número de reserva."
            chat_state["step"] = 3
        elif user_message == "3":
            response = "Para cancelar una reserva, por favor proporciona el número de reserva."
            chat_state["step"] = 4
        else:
            response = "Opción no válida. ¿Cuál es su solicitud?\n1. Reservar\n2. Modificar reserva\n3. Cancelar reserva"
    
    elif chat_state["step"] == 2:
        if user_message in ["1", "2", "3"]:
            room_types = { "1": "Sencilla", "2": "Doble", "3": "Suite" }
            response = f"Has elegido una habitación {room_types[user_message]}. Por favor ingresa tu nombre completo."
            chat_state["room_type"] = room_types[user_message]
            chat_state["step"] = 5
        else:
            response = "Opción no válida. ¿Qué tipo de habitación desea?\n1. Sencilla\n2. Doble\n3. Suite"
    
    elif chat_state["step"] == 3 or chat_state["step"] == 4:
        reference_number = user_message.strip()
        response = f"Procesando tu solicitud con número de referencia {reference_number}... (esto es un ejemplo)."
        chat_state["step"] = 0  

    elif chat_state["step"] == 5:
        name = user_message.strip()
        response = f"Gracias, {name}. Ahora ingrese las fechas de su reservación.\nFecha de entrada (DD/MM/AAAA):"
        chat_state["name"] = name
        chat_state["step"] = 6

    elif chat_state["step"] == 6:
        check_in_date_str = user_message.strip()
        try:
            check_in_date = datetime.strptime(check_in_date_str, "%d/%m/%Y")
            response = f"Fecha de entrada registrada como {check_in_date_str}. Ahora ingrese la fecha de salida (DD/MM/AAAA):"
            chat_state["check_in_date"] = check_in_date
            chat_state["step"] = 7
        except ValueError:
            response = "Formato inválido. Por favor ingrese la fecha de entrada en formato DD/MM/AAAA."

    elif chat_state["step"] == 7:
        check_out_date_str = user_message.strip()
        try:
            check_out_date = datetime.strptime(check_out_date_str, "%d/%m/%Y")
            if check_out_date > chat_state["check_in_date"]:
                room_type = chat_state.get("room_type", "")
                response = f"Reservación confirmada para una habitación {room_type} desde {chat_state['check_in_date'].strftime('%d/%m/%Y')} hasta {check_out_date.strftime('%d/%m/%Y')}.\nNúmero de referencia: {random.randint(100000,999999)}."
                chat_state["step"] = 0
            else:
                response = "La fecha de salida debe ser posterior a la fecha de entrada."
        except ValueError:
            response = "Formato inválido. Por favor ingrese la fecha de salida en formato DD/MM/AAAA."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)