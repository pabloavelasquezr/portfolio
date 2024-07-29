import reflex as rx
from portfolio.components.icon_badge import icon_badge, since_block
from portfolio.styles.style import FontSize as Size

def experience() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Experiencia",
            font_size=Size.H2.value,
        ),

        rx.flex(
            rx.hstack(
                icon_badge("brain"),
                rx.vstack(
                    rx.heading(
                        "AI Code Reviewer",
                        font_size=Size.H3.value,
                    ),
                    rx.heading(
                        "Revelo",
                        font_size=Size.H4.value,
                        color_scheme="gray",
                    ),
                    rx.list.unordered(
                        rx.list.item("Entrenar modelos de inteligencia artificial generativa en lenguaje SQL, fomentando su desarrollo como codificadores expertos y contribuyendo a la creación de herramientas de codificación avanzadas para la próxima generación."),
                        rx.list.item("Revisión de código generado por IA, concentrándose en resolver desafíos de codificación mediante la creación de soluciones de código funcionales y eficientes."),
                        rx.list.item("Desarrollo de casos de prueba sólidos para validar la eficiencia y la eficacia del código."),                    
                    ),
                )
            ),
            since_block("mayo 2024 - actualidad","map-pin","Miami, Estados Unidos"),
            flex_direction=["column-reverse", "row"],
        ),

        rx.flex(
            rx.hstack(
                icon_badge("braces"),
                rx.vstack(
                    rx.heading(
                        "Administrador de plataformas",
                        font_size=Size.H3.value,
                    ),
                    rx.heading(
                        "Universidad Externado de Colombia",
                        font_size=Size.H4.value,
                        color_scheme="gray",
                    ),
                    rx.list.unordered(
                        rx.list.item("Desarrollo de aplicaciones utilizando Python, Django, Javascript, React y MySQL."),
                        rx.list.item("Generar nuevas ideas y mejoras a los proyectos actuales."),
                        rx.list.item("Integración del directorio activo con (Wordpress/buddypress) y Moodle, mejorando el acceso de 10.000 usuarios."),
                        rx.list.item("Creación de consultas SQL, generando más de 40 reportes para uso gerencial."),
                        rx.list.item("Desarrollo de dashboards en Power BI."),
                        rx.list.item("Administración de MS Active Directory en tareas de mesa de ayuda."),
                    ),
                )
            ),
            since_block("junio 2017 - noviembre 2023","map-pin","Bogotá, Colombia"),
            flex_direction=["column-reverse", "row"],
        ),

        rx.flex(
            rx.hstack(
                icon_badge("presentation"),
                rx.vstack(
                    rx.heading(
                        "Gestor de Proyectos",
                        font_size=Size.H3.value,
                    ),
                    rx.heading(
                        "Telefónica Educación Digital",
                        font_size=Size.H4.value,
                        color_scheme="gray",
                    ),
                    rx.list.unordered(
                        rx.list.item("Informes de progreso semanales a la gerencia."),
                        rx.list.item("Gestionar los controles de calidad de los productos y los procesos de aseguramiento de la calidad en las líneas de producción."),
                        rx.list.item("Generar nuevas ideas y mejoras a los productos actuales."),
                        rx.list.item("Planificador de redes para nuevos proyectos."),
                        rx.list.item("Planificación de proyectos educativos en cada faceta, identificando los recursos necesarios, las actividades a realizar, los plazos y costes previstos en el presupuesto."),
                        rx.list.item("Manejo de buenas relaciones externas del proyecto con clientes, proveedores y subcontratistas."),
                    ),
                )
            ),
            since_block("febrero 2016 - mayo 2017","map-pin","Bogotá, Colombia"),
            flex_direction=["column-reverse", "row"],
        ),

        rx.flex(
            rx.hstack(
                icon_badge("database"),
                rx.vstack(
                    rx.heading(
                        "Administrativo y gestión",
                        font_size=Size.H3.value,
                    ),
                    rx.heading(
                        "Universidad de Valencia",
                        font_size=Size.H4.value,
                        color_scheme="gray",
                    ),
                    rx.list.unordered(
                        rx.list.item("Actividades de apoyo administrativo y de gestión educativa al Máster en Creación y Gestión de Empresas Innovadoras (Master EI)."),
                        rx.list.item("Elaboración de bases de datos para la línea de investigación “Emtrepreneurship e Innovación”."),
                    ),
                )
            ),
            since_block("febrero 2015 - mayo 2015","map-pin","Valencia, España"),
            flex_direction=["column-reverse", "row"],
        ),

        rx.flex(
            rx.hstack(
                icon_badge("code"),
                rx.vstack(
                    rx.heading(
                        "Administrador de Sistemas y Tecnologías de Información",
                        font_size=Size.H3.value,
                    ),
                    rx.heading(
                        "Universidad Autónoma de Bucaramanga, UNAB Virtual",
                        font_size=Size.H4.value,
                        color_scheme="gray",
                    ),
                    rx.list.unordered(
                        rx.list.item("Crear manuales de operación y documentos de mantenimiento."),
                        rx.list.item("Ofrecer atención al cliente, capacitación y soporte técnico para la operación, mantenimiento, uso y administración diarios en Blackboard y Moodle LMS, obteniendo un 99% de estabilidad en el servicio."),
                    ),
                )
            ),
            since_block("febrero 2011 - septiembre 2014","map-pin","Bucaramanga, Colombia"),
            flex_direction=["column-reverse", "row"],
        ),

        rx.flex(
            rx.hstack(
                icon_badge("code-xml"),
                rx.vstack(
                    rx.heading(
                        "Profesional Elearning",
                        font_size=Size.H3.value,
                    ),
                    rx.heading(
                        "Universidad Autónoma de Bucaramanga, UNAB Virtual",
                        font_size=Size.H4.value,
                        color_scheme="gray",
                    ),
                    rx.list.unordered(
                        rx.list.item("Diseño, programación y desarrollo de nuevas tecnologías para diversos proyectos en el área de e-learning en tecnologías HTML5 con manejo de API SCORM 1.2. Administración y soporte de las plataformas Blackboard y Moodle LMS."),
                    ),
                )
            ),
            since_block("octubre 2008 - enero 2011","map-pin","Bucaramanga, Colombia"),
            flex_direction=["column-reverse", "row"],
        )
    )