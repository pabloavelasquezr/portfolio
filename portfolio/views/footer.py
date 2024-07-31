import reflex as rx
from datetime import datetime as dt

def footer(data) -> rx.Component:
    return rx.hstack(
        rx.text(f"© {dt.now().year} {data.footer.author}", font_size="sm"),
        rx.text(f" - {data.footer.city} - "),
        rx.text(data.footer.made),
        justify="center",
        margin_top="60px",
        opacity= "0.5"
    )    