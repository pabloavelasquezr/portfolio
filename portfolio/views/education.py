import reflex as rx
from portfolio.components.icon_badge import icon_badge, icon_map, since_block
from portfolio.styles.style import FontSize as Size

def education() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Educación",
            font_size=Size.H2.value,
        ),
        rx.flex(
            rx.hstack(
                icon_badge("graduation-cap"),
                rx.vstack(
                    rx.text(
                        "Máster en Creación y Gestión de Empresas Innovadora"
                    ),
                    rx.text(
                        "Universidad de Valencia"
                    ),
                ),
                width="100%"
            ),
            since_block("octubre 2014 - julio 2015","map-pin","Valencia, España"),
            flex_direction=["column-reverse", "row"],width="100%"
        ),
        rx.flex(
            rx.hstack(
                icon_badge("library-big"),
                rx.vstack(
                    rx.text(
                        "Especialista en Tecnologías Avanzadas para el Desarrollo de Software"
                    ),
                    rx.text(
                        "Universidad Autónoma de Bucaramanga"
                    ),
                ),
                width="100%"
            ),
            since_block("febrero 2009 - julio 2010","map-pin","Bucaramanga, Colombia"),
            flex_direction=["column-reverse", "row"],width="100%"
        ),
        rx.flex(
            rx.hstack(
                icon_badge("book-open-check"),
                rx.vstack(
                    rx.text(
                        "Ingeniero de Sistemas"
                    ),
                    rx.text(
                        "Universitaria de Investigación y Desarrollo"
                    ),
                ),
                width="100%"
            ),
            since_block("febrero 2002 - julio 2007","map-pin","Bucaramanga, Colombia"),
            flex_direction=["column-reverse", "row"],width="100%"
        ),
        width="100%"
    )