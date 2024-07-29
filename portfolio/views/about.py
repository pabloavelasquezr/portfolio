import reflex as rx
from portfolio.styles.style import FontSize as Size

def about() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Sobre mí",
            font_size=Size.H2.value,
        ),
        rx.text(
            "lore ipsum dolor sit amet, consectetur adipiscing elit. in euismod ipsum et dui rhoncus, nec ultricies nunc ultricies. lorem ipsum dolor sit amet, consectetur adipiscing elit. in euismod ipsum et dui rhoncus, lore ipsum dolor sit amet, consectetur adipiscing elit. in euismod ipsum et dui rhoncus, nec ultricies nunc ultricies.",
        ),
    )
