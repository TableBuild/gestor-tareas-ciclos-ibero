from gestor import (
    listar_tareas,
    agregar_tarea,
    filtrar_tareas,
    exportar_csv,
    obtener_estadisticas,
    buscar_tarea_por_id,
    eliminar_tarea_con_auditoria,
)


def mostrar_menu():
    print("\n====================================================")
    print("  GESTOR DE TAREAS Y CICLOS ACADÉMICOS - IBERO")
    print("====================================================")
    print("1. Listar todas las tareas")
    print("2. Registrar nueva tarea académica")
    print("3. Filtrar tareas por estado o prioridad")
    print("4. Exportar tareas del ciclo a formato CSV")
    print("5. Ver resumen estadístico del ciclo académico")
    print("6. Eliminar tarea (con registro de auditoría)")
    print("0. Salir")
    print("====================================================")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- Listado General de Tareas ---")
            tareas = listar_tareas()
            if not tareas:
                print("No hay tareas registradas actualmente.")
            else:
                for t in tareas:
                    print(
                        f"[{t['id']}] {t['titulo']} | Materia: {t['materia']} | "
                        f"Ciclo: {t['ciclo']} | Límite: {t['fecha_limite']} | "
                        f"Prioridad: {t['prioridad']} | Estado: {t['estado']}"
                    )

        elif opcion == "2":
            print("\n--- Registrar Nueva Tarea Académica (HU-02) ---")
            try:
                titulo = input("Título de la actividad: ")
                materia = input("Asignatura: ")
                ciclo = input("Ciclo académico (ej. Ciclo 1 - 2026): ")
                fecha = input("Fecha límite (YYYY-MM-DD): ")
                prioridad = input("Prioridad (Alta / Media / Baja) [Media]: ") or "Media"
                tarea = agregar_tarea(titulo, materia, ciclo, fecha, prioridad)
                print(f"[OK] Tarea #{tarea['id']} '{tarea['titulo']}' registrada correctamente.")
            except ValueError as e:
                print(f"[Error] {e}")

        elif opcion == "3":
            print("\n--- Filtrar Tareas (HU-01) ---")
            print("1. Filtrar por estado (pendiente / en_progreso / completada)")
            print("2. Filtrar por prioridad (Alta / Media / Baja)")
            sub_opcion = input("Elija criterio (1 o 2): ").strip()

            if sub_opcion == "1":
                valor = input("Ingrese el estado a buscar: ")
                resultados = filtrar_tareas("estado", valor)
            elif sub_opcion == "2":
                valor = input("Ingrese la prioridad a buscar: ")
                resultados = filtrar_tareas("prioridad", valor)
            else:
                print("[Error] Criterio no válido.")
                continue

            if not resultados:
                print(f"No se encontraron tareas con el criterio '{valor}'.")
            else:
                for t in resultados:
                    print(
                        f"[{t['id']}] {t['titulo']} | Materia: {t['materia']} | "
                        f"Límite: {t['fecha_limite']} | Prioridad: {t['prioridad']} | Estado: {t['estado']}"
                    )

        elif opcion == "4":
            print("\n--- Exportar Cronograma a CSV (HU-04) ---")
            cantidad, ruta = exportar_csv()
            print(f"[OK] Se exportaron {cantidad} tareas correctamente en '{ruta}'.")

        elif opcion == "5":
            print("\n--- Resumen Estadístico del Ciclo (HU-05) ---")
            stats = obtener_estadisticas()
            print(f"Total de tareas registradas : {stats['total']}")
            print(f" - Pendientes               : {stats['pendientes']}")
            print(f" - En progreso              : {stats['en_progreso']}")
            print(f" - Completadas              : {stats['completadas']}")
            print(f"Porcentaje de cumplimiento  : {stats['porcentaje_cumplimiento']}%")
            if stats["vencidas"] > 0:
                print(f"[ALERTA] Tienes {stats['vencidas']} tarea(s) vencida(s) sin completar.")
            else:
                print("[OK] No tienes tareas vencidas a la fecha.")

        elif opcion == "6":
            print("\n--- Eliminar Tarea con Auditoría (HU-03) ---")
            try:
                tarea_id = int(input("Ingrese el ID de la tarea a eliminar: ").strip())
            except ValueError:
                print("[Error] El ID debe ser un número entero.")
                continue

            tarea = buscar_tarea_por_id(tarea_id)
            if not tarea:
                print(f"[Error] No existe ninguna tarea con ID #{tarea_id}.")
                continue

            confirmar = input(
                f"¿Confirma eliminar '{tarea['titulo']}' (Materia: {tarea['materia']})? [S/N]: "
            ).strip().lower()

            if confirmar == "s":
                eliminada = eliminar_tarea_con_auditoria(tarea_id)
                print(f"[OK] Tarea #{eliminada['id']} eliminada y registrada en 'auditoria.log'.")
            else:
                print("Operación cancelada. La tarea no fue eliminada.")

        elif opcion == "0":
            print("Saliendo del Gestor Académico. ¡Éxitos en el ciclo!")
            break
        else:
            print("[Error] Opción no válida. Intente nuevamente.")


if __name__ == "_main_":
    main()