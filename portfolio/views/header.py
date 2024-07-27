import reflex as rx
from portfolio.components.icon_badge import icon_map
from portfolio.styles.style import TextColor


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="pablo_avatar.jpg",
                size="7",
                border="1px solid",
                border_color=rx.color_mode_cond(
                    light=TextColor.LIGHT.value, 
                    dark=TextColor.DARK.value
                )
            ),
            rx.vstack(
                rx.heading("Pablo Velásquez", size="6"),
                rx.text(
                    "Software Developer | Python | Systems Engineer | LMS | E-Learning"
                ),
                icon_map("map-pin"," Bucaramanga, Colombia"),
                rx.hstack(
                    
                    rx.link(
                        rx.tooltip(
                            rx.button(rx.icon("mail"),"pabloavelasquez@gmail.com",variant="solid"), 
                            content="Email",
                        ),
                        href="mailto:pabloavelasquez@gmail.com",is_external=True
                    ),
                    rx.link(
                        rx.tooltip(
                            rx.button(rx.icon("file-text"),variant="surface"), 
                            content="Hoja de vida",
                        ),
                        href="assets/CV_pablo_velasquez_en.pdf",is_external=True
                    ),
                    rx.link(
                        rx.tooltip(
                            rx.button(rx.icon("github"),variant="surface"), 
                            content="GitHub",
                        ),
                        href="https://github.com/pabloavelasquezr",is_external=True
                    ),
                    rx.link(
                        rx.tooltip(
                            rx.button(rx.icon("linkedin"),variant="surface"), 
                            content="LinkedIn",
                        ),
                        href="https://www.linkedin.com/in/pabloavelasquez/",is_external=True
                    ),
                    flex_wrap="wrap",
                ),
                align_items="start",

            ),
            
        )
    )