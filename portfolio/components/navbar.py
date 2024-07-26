import reflex as rx

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
        background_color=rx.color_mode_cond(light="#f2f2f2", dark="#121212"),
    )