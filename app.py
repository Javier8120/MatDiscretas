from flask import Flask, render_template as render, flash, request, redirect, url_for
from math import gcd 
app = Flask(__name__)
app.secret_key = 'sfnsfisni3n4i3nsowdo2023iofmcim4i4903fm394mfoe'

   
#Rutas generales :v


@app.route('/', methods=["GET", "POST"])
def Login():
    flash("Bienvenido", category='info')
    return render("index.html", methods=["GET", "POST"])


@app.route('/Problema1', methods=["GET", "POST"])
def ruta1():
    return render("DecimalesInfinitos.html")



@app.route("/Problema1/procesar", methods=["POST"])
def procesar():
    PenteraString = request.form.get("Pentera", int())
    PeriodoString = request.form.get("Periodo", int())
    Pentera = int(PenteraString)
    Periodo = int(PeriodoString)

    lista=[9, 99, 999, 9999, 99999, 999999]
    error=False
    if Periodo < 0:
        error = True
        flash("Ehhh, la parte fraccionaria no puede ser 0 ", category='info')
    elif Periodo == 0:
        error = True
        flash(":V Si el periodo es 0 entonces la fracciones es la Parte entera sobre 1.(ParteEntera/1)", category='error')
    elif Periodo >=1000000:
        flash("Estamos trabajando con numeros entre 1 y 999999")
    elif Periodo < 10 and Periodo > 0:
        numerador=lista[0]
    elif Periodo < 100 and Periodo >= 10:
        numerador=lista[1]
    elif Periodo < 1000 and Periodo >= 100:
        numerador=lista[2]
    elif Periodo < 10000 and Periodo >= 1000:
        numerador=lista[3]
    elif Periodo < 100000 and Periodo >= 10000:
        numerador=lista[4]
    elif Periodo < 1000000 and Periodo >= 100000:
        numerador=lista[5]
    if Pentera == 0 and error==False:
        denominador1= Periodo
        denominador_fraccion1 = (denominador1-Pentera)
        mcd1 = gcd(denominador1,numerador)
        denominador_simplificado1 = int(denominador1/mcd1)
        numerador_simplificado1 = int(numerador/mcd1)
        fraccion_simplificada1= (f"{denominador_simplificado1}/{numerador_simplificado1}")
        flash(f"La fraccion resultante de : {Pentera},{Periodo}... es:  {denominador_fraccion1}/{numerador} y la Fraccion simplificada es: {fraccion_simplificada1}", category='success')
    
    elif Pentera != 0 and error==False:
        denominador = int(f"{Pentera}{Periodo}")
        denominador_fraccion = (denominador-Pentera)
        mcd = gcd(denominador,numerador)
        denominador_simplificado = int(denominador/mcd)
        numerador_simplificado =   int(numerador/mcd)
        fraccion_simplificada= (f"{denominador_simplificado}/{numerador_simplificado}")
        flash(f"La fraccion resultante de : {Pentera},{Periodo}...  es: {denominador_fraccion}/{numerador} y la Fraccion simplificada es: {fraccion_simplificada} ", category='success')


    return redirect("/Problema1")
    
