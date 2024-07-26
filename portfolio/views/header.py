import reflex as rx
from portfolio.components.icon_badge import icon_map

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="pablo_avatar.jpg",
                size="7",
                radius="full",
                border= "1px solid white",
                border_color=rx.color_mode_cond(light="#444750", dark="#d9d9d9")
            ),
            rx.vstack(
                rx.heading("Pablo Velásquez", size="lg"),
                rx.text(
                    "Software Developer | Python | Systems Engineer | LMS | E-Learning"
                ),
                icon_map("map-pin"," Bucaramanga, Colombia"),
                rx.text(
                    "pabloavelasquez@gmail.com",
                ),
                align_items="start",
            ),
            
        )
    )