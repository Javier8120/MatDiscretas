# Configuracion por defecto para flask 

from flask import Flask, render_template as render
app = Flask(__name__)
app.secret_key = 'Equipo8'

   
#Crear Ruta
@app.route('/Loquesea', methods=["GET", "POST"])
def Loquesea():
    return render("loquesea.html")

# .gitignore cumple la funcion de obviar o ignorar las carpetas del proyecto que alli se comenten.
# index es la vista principal
# layout es el diseño por defecto, para futuras actualizciones.
# El archivo Procfile nos genera la conexion con Heroku... para poder desplegar nuestra app en la web 


