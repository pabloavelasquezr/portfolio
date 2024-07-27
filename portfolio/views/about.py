import reflex as rx

def about() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Sobre mí",
            size="5",
        ),
        rx.text(
            "lore ipsum dolor sit amet, consectetur adipiscing elit. in euismod ipsum et dui rhoncus, nec ultricies nunc ultricies. lorem ipsum dolor sit amet, consectetur adipiscing elit. in euismod ipsum et dui rhoncus, lore ipsum dolor sit amet, consectetur adipiscing elit. in euismod ipsum et dui rhoncus, nec ultricies nunc ultricies.",size="2",
        ),
    )
