# Historias de Usuario (HU)

## Gestor de tareas y ciclos académicos (CLI en Python)

Este documento presenta las **Historias de Usuario (HU)** definidas para el desarrollo del proyecto *Gestor de tareas y ciclos académicos*. Las historias se encuentran organizadas cronológicamente de acuerdo con el ciclo de vida de los datos dentro del sistema:

**Creación → Consulta y filtrado → Exportación → Análisis estadístico → Eliminación con auditoría**

---

## Matriz de Historias de Usuario

| ID | Clave | Título | Historia de Usuario | Criterios de aceptación | Prioridad | Estimación | Responsable |
|------|------|------|------|------|------|------|------|
| **HU-02** | GTC-01 | Registro de una nueva tarea académica | **Como** estudiante de ingeniería de software, **quiero** registrar una nueva tarea académica ingresando título, asignatura, ciclo académico, fecha límite y prioridad, **para** mantener organizados mis entregables universitarios dentro del sistema. | 1. El sistema asigna automáticamente un identificador numérico consecutivo.<br>2. El estado inicial de la tarea debe ser `pendiente`.<br>3. Se valida que el título y la asignatura no estén vacíos.<br>4. La información se almacena en `tareas.json`.<br>5. La funcionalidad está disponible mediante la opción correspondiente del menú principal. | Alta | 3 pts  | Mariana González Calderón |
| **HU-01** | GTC-02 | Filtrado de tareas por estado y prioridad | **Como** estudiante universitario, **quiero** filtrar mis tareas por estado o prioridad, **para** identificar rápidamente las actividades que requieren atención inmediata. | 1. Permite filtrar por estado (`pendiente`, `en_progreso`, `completada`).<br>2. Permite filtrar por prioridad (`Alta`, `Media`, `Baja`).<br>3. Solo se muestran las tareas que coinciden con el criterio seleccionado.<br>4. Si no existen coincidencias, el sistema informa al usuario sin finalizar la ejecución del programa. | Alta | 3 pts  | Omar Dario Mesa Gomez |
| **HU-04** | GTC-03 | Exportación de tareas del ciclo a formato CSV | **Como** estudiante organizado, **quiero** exportar las tareas registradas a un archivo CSV, **para** analizarlas, compartirlas o utilizarlas en aplicaciones de hoja de cálculo. | 1. El sistema genera el archivo `reporte_ciclo.csv`.<br>2. El archivo contiene los encabezados: ID, Título, Materia, Ciclo, Fecha_Límite, Prioridad y Estado.<br>3. La exportación se realiza con codificación UTF-8.<br>4. El archivo exportado es ignorado por Git mediante `.gitignore`. | Media | 2 pts  | Omar Dario Mesa Gomez / Mariana González Calderón |
| **HU-05** | GTC-04 | Resumen estadístico de avance del ciclo académico | **Como** estudiante que monitorea su desempeño académico, **quiero** visualizar estadísticas de mis tareas, **para** conocer mi nivel de cumplimiento y detectar actividades pendientes o vencidas. | 1. Muestra el número total de tareas registradas.<br>2. Muestra la cantidad de tareas por estado.<br>3. Calcula el porcentaje de cumplimiento.<br>4. Identifica tareas vencidas comparando la fecha límite con la fecha actual.<br>5. Gestiona correctamente escenarios sin tareas registradas. | Media | 3 pts  | Elian Felipe Gómez Recalde  |
| **HU-03** | GTC-05 | Eliminación segura de tareas con auditoría | **Como** usuario del sistema, **quiero** eliminar una tarea mediante confirmación previa y registrar la acción en un archivo de auditoría, **para** conservar la trazabilidad de los cambios realizados. | 1. Solicita confirmación antes de eliminar una tarea.<br>2. Muestra el título asociado al ID seleccionado.<br>3. Registra fecha, hora, ID y título en `auditoria.log`.<br>4. Informa cuando el ID ingresado no existe.<br>5. La eliminación se ejecuta únicamente tras la confirmación del usuario. | Baja | 2 pts  | Elian Felipe Gómez Recalde  |

---

## Resumen de Priorización

| Prioridad | Cantidad |
|------------|------------|
| Alta | 2 |
| Media | 2 |
| Baja | 1 |

---

## Equipo de Desarrollo

| Integrante | Responsabilidades |
|-------------|------------------|
| Mariana González Calderón | Registro de tareas académicas y exportación CSV |
| Omar Dario Mesa Gomez                      | Filtrado de tareas y exportación CSV                                     |
| Elian Felipe Gómez Recalde  | Resumen estadístico y auditoría de eliminación |
|   |  |

---

## Observaciones

- Las historias fueron definidas bajo el formato **Como / Quiero / Para**.
- La priorización se realizó considerando el flujo principal de uso del sistema.
- Las estimaciones corresponden al esfuerzo previsto para la implementación de cada funcionalidad dentro del proyecto académico.
- El orden de las historias refleja la secuencia natural de operación del sistema y facilita su implementación incremental.