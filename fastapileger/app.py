from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime
from uuid import uuid4 as uuid
import uvicorn
#print("test");
app = FastAPI()
registros = [] #este es el arreglo donde se guarda la data(cuando se reinicia la app se limpia)

# Post model
class Post(BaseModel):
    id: str
    nombre: str
    apellido: str
    sexo: str
    edad: str
    fecha_creacion: datetime =  datetime.now() #get fecha actual


@app.get('/') #prueba get raiz jejeje
def welcome_test():
    return {"welcome": "FastApi Rest"}


@app.get('/registros') #get de todos los registros
def get_registros_all():
    return registros


@app.post('/registros')
def post_registros(post: Post):
   # post.id = str(uuid()) # descomentar para que el id sea autogenerado random string
    registros.append(post.dict())
    return registros[-1]


@app.get('/registros/{id}') #get registro con id especifico
def get_registro_by_id(id: str):
   # def get_post(id: str):
    for post in registros:
        if post["id"] == id:
            return post
    raise HTTPException(status_code=404, detail="Item not found")


@app.put('/registros/{id}') #actualizar un registro
def update_registro(id: str, updatedPost: Post):
    for index, post in enumerate(registros):
        if post["id"] == id:
            registros[index]["nombre"]= updatedPost.dict()["nombre"]
            registros[index]["apellido"]= updatedPost.dict()["apellido"]
            registros[index]["sexo"]= updatedPost.dict()["sexo"]
            registros[index]["edad"]= updatedPost.dict()["edad"]
            return {"Mensaje": "Elemento actualizado de manera satistactoria"}
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete('/registros/{id}') #eliminar un registro
def delete_registro(id: str):
    for index, post in enumerate(registros):
        if post["id"] == id:
            registros.pop(index)
            return {"Mensaje": "Elemento eliminado de manera satisfactoria"}
    raise HTTPException(status_code=404, detail="Item not found")





