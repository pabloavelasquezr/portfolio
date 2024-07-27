import reflex as rx

def skills() -> rx.Component:
    return rx.vstack(
            rx.heading(
                "Competencias",
                size="5",
            ),
            
            rx.list.unordered(
                rx.list.item("Capacidad para trabajar en un equipo multidisciplinar, buscando el éxito del grupo en cada proyecto."),
                rx.list.item("Trabajador muy dinámico, proactivo, ingenioso, muy buen evaluador del tiempo necesario para realizar las tareas, analítico, metódico, riguroso y detallista, sentido de la iniciativa, adaptabilidad, con buenas dotes de comunicación."),
                rx.list.item("Evangelista de back-end de Python: lógica orientada a subprocesos de bajo nivel, ciencia de datos, multiprocesamiento, API, integración de sistemas."),
                rx.list.item("Fuertes habilidades en HTML, JavaScript, PHP, CSS."),
                rx.list.item("Habilidades y conocimientos promedio en Python."),
                rx.list.item("Diseño, implementación y mantenimiento de bases de datos MongoDB y MySQL."),
                rx.list.item("Muy familiarizado con Microsoft Power BI."),
                rx.list.item("Programación de macros en MS Office."),
                rx.list.item("Administración de MS Active Directory en tareas de mesa de ayuda."),
            ),
    )