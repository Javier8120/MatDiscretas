from flask import Flask, render_template as render, flash as alerta
app = Flask(__name__)
app.secret_key = 'sfnsfisni3n4i3nsowdo2023iofmcim4i4903fm394mfoe'

   
#Rutas generales :v

@app.route('/', methods=["GET", "POST"])
def Login():
    return render("index.html")