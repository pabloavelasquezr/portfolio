import reflex as rx
from portfolio.styles.style import FontSize as Size

def about(data) -> rx.Component:
    return rx.vstack(
        rx.heading(
            data.abouttitle,
            font_size=Size.H2.value,
        ),
        rx.text(
            data.about,
        ),
    )
