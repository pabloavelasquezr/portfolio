import reflex as rx
from datetime import datetime as dt

def footer() -> rx.Component:
    return rx.hstack(
        rx.text(f"© {dt.now().year} Pablo Velasquez", font_size="sm"),
        rx.text(" - 📍Bucaramanga, Colombia - "),
        rx.text("hecho en Reflex y Python🐍 con ❤️"),
        justify="center",
        margin_top="60px",
        opacity= "0.5"
    )    