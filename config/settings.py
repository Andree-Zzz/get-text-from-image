import os
from dotenv import load_dotenv

#Cargar el archivo .env a las variables de entorno
load_dotenv()

PATH_TESSERACT_CMD = os.environ.get('PATH_TESSERACT_CMD')