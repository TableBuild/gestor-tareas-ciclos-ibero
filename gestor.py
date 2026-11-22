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


def agregar_tarea(titulo, materia, ciclo, fecha_limite, prioridad="Media"):
    """Registra una nueva tarea academica con validacion basica y estado 'pendiente'."""

    if not titulo.strip() and not materia.strip():
        raise ValueError("El titulo y la asignatura son campos obligatorios.")
    if not titulo.strip():
        raise ValueError("El titulo de la actividad no puede estar vacío.")
    if not materia.strip():
        raise ValueError("La asignatura no puede estar vacía.")

    tareas = cargar_tareas()
    nuevo_id = 1 if not tareas else max(t["id"] for t in tareas) + 1

    nueva_tarea = {
        "id": nuevo_id,
        "titulo": titulo.strip(),
        "materia": materia.strip(),
        "ciclo": ciclo.strip() or "Ciclo General",
        "fecha_limite": fecha_limite.strip(),
        "prioridad": prioridad.strip() or "Media",
        "estado": "pendiente"
    }

    tareas.append(nueva_tarea)
    guardar_tareas(tareas)

    return nueva_tarea