import json
import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# Nom del fitxer on desarem/carregarem dades
dicAlumnes = "alumnes.json"

# Inicialitzem la llista d'alumnes
alumnat = []

# Modelo base para el ADD
class Alumne(BaseModel):
 nom: str
 cognom: str
 dia: int
 mes: int
 any: int
 email: str
 feina: str
 curs: int


# Carreguem les dades si el fitxer existeix
if os.path.exists(dicAlumnes):
    with open(dicAlumnes, "r") as f:
        alumnat = json.load(f)

# Mostrar el texto Institut TIC de Barcelona
@app.get("/")
def index():
    return "Institut TIC de Barcelona"

# Mostrar el numero de alumnos totales
@app.get("/alumnes/")
def get_total_alumnes():
    return {"total": len(alumnat)}

# Muestra la informacion de un Alumno en concreto usando el ID como referencia
@app.get("/id/{numero}")
def get_alumne(numero: int):
    for alumne in alumnat:
        if alumne["id"] == numero:
            return alumne
    return {"error": f"No s'ha trobat cap alumne amb ID {numero}"} # Mensaje de error


@app.delete("/del/{numero}")
def delete_alumne(numero: int):
    global alumnat
    for i, alumne in enumerate(alumnat): # recorre la lista
        if alumne["id"] == numero: # si ID coincide con el numero proporcionado
            del alumnat[i] # elimina el alumno asociado al ID del mismo numero proporcionado
            with open(dicAlumnes, "w") as f:  # abre el archivo en mode escritura y guarda el contenido de forma estructurada
                json.dump(alumnat, f, indent=4)
            return {"missatge": "Alumne eliminat correctament"} # mensaje de confirmacion
    return {"error": f"No s'ha trobat cap alumne amb ID {numero}"}  # Mensaje de error

#
@app.post("/alumne/")
def post_alumne(alumne: Alumne):
    nou_id = max([a["id"] for a in alumnat], default=0) + 1
    alumne_dict = alumne.dict()
    alumne_dict["id"] = nou_id
    alumne_dict = {"id": alumne_dict["id"], **alumne_dict}    # Mover el ID al principio del diccionario
    alumnat.insert(0, alumne_dict)    # Añadir el alumno al principio de la lista
    with open(dicAlumnes, "w") as f:    # Guardar los alumnes en el archivo
        json.dump(alumnat, f, indent=4)
    return {"missatge": "Alumne afegit correctament", "id": nou_id}    # mostrar un texto
