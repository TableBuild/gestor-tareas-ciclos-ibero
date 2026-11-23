import csv
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
    """Registra una nueva tarea académica con validación básica y estado 'pendiente'."""
    if not titulo.strip() or not materia.strip():
        raise ValueError("El título y la asignatura son obligatorios.")

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


def filtrar_tareas(criterio, valor):
    """Filtra las tareas por 'estado' o 'prioridad' sin distinguir mayúsculas/minúsculas (HU-01)."""
    tareas = cargar_tareas()
    valor_normalizado = valor.strip().lower()
    return [
        t for t in tareas
        if str(t.get(criterio, "")).strip().lower() == valor_normalizado
    ]


def exportar_csv(nombre_archivo="reporte_ciclo.csv"):
    """Exporta todas las tareas registradas a un archivo CSV en UTF-8 (HU-04)."""
    tareas = cargar_tareas()
    encabezados = ["ID", "Titulo", "Materia", "Ciclo", "Fecha_Limite", "Prioridad", "Estado"]

    with open(nombre_archivo, mode="w", newline="", encoding="utf-8-sig") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(encabezados)
        for t in tareas:
            escritor.writerow([
                t["id"],
                t["titulo"],
                t["materia"],
                t["ciclo"],
                t["fecha_limite"],
                t["prioridad"],
                t["estado"]
            ])
    return len(tareas), nombre_archivo