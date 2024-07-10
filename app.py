from flask import Flask, render_template

app = Flask(__name__)

# Lista de combinaciones de fantasmas y evidencias
combinaciones = {
    "Espiritu": ["Escritura fantasma", "EMF Nivel 5", "Spirit Box"],
    "Espectro": ["EMF Nivel 5", "Proyector D.O.T.S.", "Spirit Box"],
    "Ente": ["Proyector D.O.T.S.", "Huellas dactilares", "Spirit Box"],
    "Poltergeist": ["Huellas dactilares", "Spirit Box", "Escritura fantasma"],
    "Banshee": ["Orbes espectrales", "Huellas dactilares", "Proyector D.O.T.S."],
    "Jinn": ["Temperaturas bajo cero", "EMF Nivel 5", "Huellas dactilares"],
    "Pesadilla": ["Orbes espectrales", "Escritura fantasma", "Spirit Box"],
    "Revenant": ["Escritura fantasma", "Temperaturas bajo cero", "Orbes espectrales"],
    "Sombra": ["Escritura fantasma", "EMF Nivel 5", "Temperaturas bajo cero"],
    "Demonio": ["Temperaturas bajo cero", "Escritura fantasma", "Huellas dactilares"],
    "Yurei": ["Orbes espectrales", "Proyector D.O.T.S.", "Temperaturas bajo cero"],
    "Oni": ["Proyector D.O.T.S.", "Temperaturas bajo cero", "EMF Nivel 5"],
    "Yokai": ["Orbes espectrales", "Spirit Box", "Proyector D.O.T.S."],
    "Hantu": ["Huellas dactilares", "Temperaturas bajo cero", "Orbes espectrales"],
    "Goryo": ["EMF Nivel 5", "Proyector D.O.T.S.", "Huellas dactilares"],
    "Myling": ["Escritura fantasma", "Huellas dactilares", "EMF Nivel 5"],
    "Onryo": ["Spirit Box", "Temperaturas bajo cero", "Orbes espectrales"],
    "Gemelos": ["Spirit Box", "Temperaturas bajo cero", "EMF Nivel 5"],
    "Raiju": ["Proyector D.O.T.S.", "Orbes espectrales", "EMF Nivel 5"],
    "Obake": ["Huellas dactilares", "EMF Nivel 5", "Orbes espectrales"],
    "Mímico": ["Spirit Box", "Huellas dactilares", "Temperaturas bajo cero"],
    "Moroi": ["Spirit Box", "Temperaturas bajo cero", "Escritura fantasma"],
    "Deogen": ["Spirit Box", "Escritura fantasma", "Proyector D.O.T.S."],
    "Thaye": ["Orbes espectrales", "Escritura fantasma", "Proyector D.O.T.S."]
}



# Ruta para renderizar index.html
@app.route('/')
def index():
    return render_template('index.html', combinaciones=combinaciones)

if __name__ == '__main__':
    app.run(debug=True)
