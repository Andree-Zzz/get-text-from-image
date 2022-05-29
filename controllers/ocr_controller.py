from datetime import datetime
from itertools import count

from PIL import Image
import pytesseract

from config.settings import PATH_TESSERACT_CMD

# Guardar la imagen del formulario y asi poder hacer el proceso de
# deteccion del texto.
def saveImage(image):
    code_date = str(datetime.now().day)+str(datetime.now().month)+str(datetime.now().hour)+str(datetime.now().second)+str(datetime.now().microsecond)
    pathfile = '/static/images/'+code_date+image.filename
    image.save(f'.{pathfile}')
    return pathfile

# Obtener el texto de la imagen
# pidiendo como parametro su ubicacion de guardado
def getTextImage(pathImage) -> str:
    img = Image.open(f'.{pathImage}')
    # Acceso a la biblioteca ejecutable de tesseract ocr
    # La cual tiene las funciones de reconocimiento
    pytesseract.pytesseract.tesseract_cmd = PATH_TESSERACT_CMD
    # Procesar la imagen para obeneter el texto
    # con la funcion que dispone pytesseract
    text_image = pytesseract.image_to_string(img, lang='spa').strip()
    # Remove remove non-ASCII characters but leave periods and spaces
    text_image = text_image.encode('ascii', errors='ignore').decode() 
    if len(text_image) == 0:
        return '*'
    else:
        return text_image
    # print(f'txtImg:{text_image}#')