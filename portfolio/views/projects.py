import reflex as rx
from portfolio.components.icon_badge import icon_badge, icon_button, icon_stack_exp
from portfolio.styles.style import FontSize as Size

def projects() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Proyectos",
            font_size=Size.H2.value,
        ),
        rx.hstack(
            icon_badge("monitor-play"),
            rx.vstack(
                rx.text(
                    "Streaming-Service"
                ),
                rx.text(
                    "(PHP Laravel MySQL y Bootstrap) **XAMPP 8.2 / PHP 8.2**"
                ),
                rx.hstack(
                    icon_stack_exp("devicon-php-plain","PHP"),
                    icon_stack_exp("devicon-laravel-plain","Laravel"),
                    icon_stack_exp("devicon-mysql-plain","MySQL"),
                    icon_stack_exp("devicon-bootstrap-plain","Bootstrap"),
                ),
                rx.hstack(
                    icon_button("link","Streaming-Service","http://animestream.wuaze.com"),
                    icon_button("github","GitHub Streaming-Service","https://github.com/pabloavelasquezr/Streaming-Service"),
                )
            )
        ),
        width="100%"
    )