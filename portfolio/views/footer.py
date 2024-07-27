import reflex as rx
from datetime import datetime as dt

def footer() -> rx.Component:
    return rx.hstack(
        rx.text(f"© {dt.now().year} Pablo Velasquez", font_size="md"),
        justify="center",
        margin_top="50px",
    )    