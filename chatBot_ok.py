from flask import Flask, request, jsonify, url_for, render_template

app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data['message']
    
    # Aquí puedes agregar lógica para generar respuestas del chatbot
    bot_response = "Esta es una respuesta del bot a tu mensaje: " + user_message
    
    return jsonify({'reply': bot_response})




if(__name__ == '__main__'):
    app.run(debug=True)