from gestor import listar_tareas


def mostrar_menu():
    print("\n====================================================")
    print("  GESTOR DE TAREAS Y CICLOS ACADÉMICOS - IBERO")
    print("====================================================")
    print("1. Listar todas las tareas")
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

        elif opcion == "0":
            print("Saliendo del Gestor Académico. ¡Éxitos en el ciclo!")
            break
        else:
            print("[Error] Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()