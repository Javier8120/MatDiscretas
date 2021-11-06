from flask import Flask, render_template as render
app = Flask(__name__)
app.secret_key = 'Equipo8'

   
#Rutas generales :v

@app.route('/', methods=["GET", "POST"])
def Login():
    return render("index.html")