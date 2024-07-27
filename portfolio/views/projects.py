import reflex as rx
from portfolio.components.icon_badge import icon_badge

def projects() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Proyectos",
            size="5",
        ),
        rx.hstack(
            icon_badge("monitor-play"),
            rx.vstack(
                rx.text(
                    "streaming-service"
                ),
                rx.text(
                    "(PHP Laravel MariaDB y Bootstrap) **XAMPP 8.2 / PHP 8.2**"
                ),
                rx.text(
                    "animestream.wuaze.com"
                ),
            )
        ),
        width="100%"
    )