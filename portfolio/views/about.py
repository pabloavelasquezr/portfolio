import reflex as rx
from portfolio.styles.style import FontSize as Size

def about() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Sobre mí",
            font_size=Size.H2.value,
        ),
        rx.text(
            "Soy un desarrollador de software con experiencia en el desarrollo de aplicaciones web con enfasis en el backend.",
        ),
    )
