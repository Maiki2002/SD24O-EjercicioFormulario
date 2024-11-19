from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional
from pydantic import BaseModel
import shutil
import os # Para acceder a la ruta del home 
import uuid

# creación del servidor
app = FastAPI()

@app.post("/foto-usuario")
async def guarda_foto(nombre:str=Form(...),direccion:str=Form(...),fotografia:UploadFile=File(...),vip:Optional[str]=Form(None)):
    print("Nombre:", nombre)
    print("Direccion:", direccion)
    print("Vip:", vip)
    vip = vip == "true"
    home_usuario = os.path.expanduser("~") #home usuario
    nombre_archivo = uuid.uuid4() #nombre del formato hexadecimal
    extension_foto = os.path.splitext(fotografia.filename)[1]
    if vip:
        ruta_imagen = f'{home_usuario}/fotos-usuarios-vip/{nombre_archivo}{extension_foto}'
    else:
        ruta_imagen = f'{home_usuario}/fotos-usuarios/{nombre_archivo}{extension_foto}'

    print("Guardado la foto en ", ruta_imagen)
    with open(ruta_imagen,"wb") as imagen:
        contenido = await fotografia.read()
        imagen.write(contenido)

    respuesta = {
        "Nombre" : nombre,
        "Direccion": direccion,
        "Ruta": ruta_imagen,
        "Vip": vip
    }
    return respuesta

# decorator
@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "hola mundo!"
    }

    return respuesta