import reflex as rx
from portfolio.components.icon_badge import icon_badge, icon_button, icon_stack_exp
from portfolio.styles.style import FontSize as Size

def projects() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Proyectos",
            font_size=Size.H2.value,
        ),
        rx.flex(
            rx.hstack(
                icon_badge("monitor-play"),
                rx.vstack(
                    rx.heading(
                        "Streaming-Service",
                        font_size=Size.H3.value,
                    ),
                    rx.text(
                        "Sistema de visualización de animes, con panel de administración y sistema de comentarios. Hecho bajo CRUD."
                    ),
                    rx.hstack(
                        icon_stack_exp("devicon-php-plain","PHP"),
                        icon_stack_exp("devicon-laravel-plain","Laravel"),
                        icon_stack_exp("devicon-mysql-plain","MySQL"),
                        icon_stack_exp("devicon-bootstrap-plain","Bootstrap"),
                        flex_wrap="wrap",
                    ),
                    rx.hstack(
                        icon_button("link","Streaming-Service","http://animestream.wuaze.com"),
                        icon_button("github","GitHub Streaming-Service","https://github.com/pabloavelasquezr/Streaming-Service"),
                        flex_wrap="wrap",
                    ),
                ),
            ),
            rx.vstack(
                rx.card(
                    rx.image(
                        src="streaming_service_thumbnail.jpg",
                        border_radius="10px",
                    ),
                    width= "max-content",
                ),
                align_items="end",
                min_width="334px"
            ),
            flex_direction=["column", "column", "row", "row", "row"],
            gap = "var(--space-3);"
        ),

        gap = "var(--space-6);"
    )