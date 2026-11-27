import csv
import json
import os
from datetime import datetime

ARCHIVO_DATOS = "tareas.json"
ARCHIVO_LOG = "auditoria.log"


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
    """Registra una nueva tarea académica con validación básica y estado 'pendiente' (HU-02)."""
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


def obtener_estadisticas():
    """Calcula métricas de cumplimiento y detecta tareas pendientes vencidas (HU-05)."""
    tareas = cargar_tareas()
    total = len(tareas)
    if total == 0:
        return {
            "total": 0,
            "pendientes": 0,
            "en_progreso": 0,
            "completadas": 0,
            "porcentaje_cumplimiento": 0.0,
            "vencidas": 0
        }

    pendientes = sum(1 for t in tareas if t["estado"].lower() == "pendiente")
    en_progreso = sum(1 for t in tareas if t["estado"].lower() == "en_progreso")
    completadas = sum(1 for t in tareas if t["estado"].lower() == "completada")
    porcentaje = round((completadas / total) * 100, 2)

    hoy = datetime.now().strftime("%Y-%m-%d")
    vencidas = 0
    for t in tareas:
        if t["estado"].lower() != "completada" and t.get("fecha_limite"):
            if t["fecha_limite"] < hoy:
                vencidas += 1

    return {
        "total": total,
        "pendientes": pendientes,
        "en_progreso": en_progreso,
        "completadas": completadas,
        "porcentaje_cumplimiento": porcentaje,
        "vencidas": vencidas
    }


def buscar_tarea_por_id(tarea_id):
    """Busca y retorna una tarea por su identificador numérico."""
    for t in cargar_tareas():
        if t["id"] == tarea_id:
            return t
    return None


def eliminar_tarea_con_auditoria(tarea_id):
    """Elimina una tarea por ID y guarda trazabilidad en auditoria.log (HU-03)."""
    tareas = cargar_tareas()
    tarea_eliminada = None
    nuevas_tareas = []

    for t in tareas:
        if t["id"] == tarea_id:
            tarea_eliminada = t
        else:
            nuevas_tareas.append(t)

    if not tarea_eliminada:
        return None

    guardar_tareas(nuevas_tareas)
    marca_tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea_log = (
        f"[{marca_tiempo}] ELIMINACION | ID: {tarea_eliminada['id']} | "
        f"Titulo: '{tarea_eliminada['titulo']}' | Materia: '{tarea_eliminada['materia']}'\n"
    )
    with open(ARCHIVO_LOG, "a", encoding="utf-8") as log_file:
        log_file.write(linea_log)

    return tarea_eliminada