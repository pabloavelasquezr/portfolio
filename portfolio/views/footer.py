import reflex as rx

def footer() -> rx.Component:
    return rx.hstack(
        rx.text("© 2024 Pablo Velasquez", font_size="md"),
        #rx.logo(),
    )    