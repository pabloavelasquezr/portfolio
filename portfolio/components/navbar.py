import reflex as rx
from portfolio.styles.style import Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text("pablo", as_="span"),
            rx.text("a", as_="span"),
            rx.text("velasquez", as_="span"),
        ),
        rx.box(
            rx.color_mode.button(),
        ),
        justify="between",
        align="center",
        position="sticky",
        z_index="999",
        top="0",
        background_color=rx.color_mode_cond(
            light=Color.BACKGROUND_LIGHT.value, 
            dark=Color.BACKGROUND_DARK.value
        ),
    )