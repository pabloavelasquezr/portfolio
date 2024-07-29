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
                        flex_wrap="wrap",
                    ),
                    rx.hstack(
                        icon_button("link","Streaming-Service","http://animestream.wuaze.com"),
                        icon_button("github","GitHub Streaming-Service","https://github.com/pabloavelasquezr/Streaming-Service"),
                        flex_wrap="wrap",
                    ),
                ),
            ),
            rx.card(
                rx.hover_card.root(
                    rx.hover_card.trigger(
                        rx.image(
                            src="/streaming_service_thumbnail.jpg",
                        ),
                    ),
                    rx.hover_card.content(
                        rx.image(src="/streaming_service.png"),
                    ),
                ),
                max_width="350px"
            ),
            width="100%",
            justify="between",
            flex_wrap="wrap",
        ),
        width="100%"
    )