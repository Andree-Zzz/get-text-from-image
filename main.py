from flask import Flask, redirect, render_template, request, url_for
from controllers import ocr_controller

app = Flask(__name__)

# Pagina inicial con el formulario de seleccion de la imagen
# a procesar
@app.get("/")
def index():
    return render_template('index.html')

# Pagina que recibe la imagen enviada en el formulario 
# y hace el respectivo procesamiento.
@app.post("/")
def procesar_imagen():
    # Obtener la imagen del formulario
    imagen = request.files['imagen']
    # Evaluar si envio una imagen o no dentro del formulario
    if imagen:
        # Guardar la imagen y obtener su ruta de ubicacion
        pathImage = ocr_controller.saveImage(imagen)
        # Procesar la imagen y obtener su texto 
        # recibiendo su ruta de ubicacion (por ahora Funciona con texto en Ingles)
        text_image = ocr_controller.getTextImage(pathImage)
        return render_template('index.html', text_image = text_image, pathImage = pathImage)
    else:
        return redirect(url_for('index'))

# app.run(debug=True) #Comentar para deplieges a Heroku
