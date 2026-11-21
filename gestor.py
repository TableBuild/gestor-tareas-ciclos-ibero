import json
import os

ARCHIVO_DATOS = "tareas.json"


def cargar_tareas():
    """Carga la lista de tareas desde el archivo JSON local."""
    if not os.path.exists(ARCHIVO_DATOS):
        return []
    with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            return []


def guardar_tareas(tareas):
    """Guarda la lista actualizada de tareas en el archivo JSON."""
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)


def listar_tareas():
    """Retorna todas las tareas registradas en el ciclo académico."""
    return cargar_tareas()