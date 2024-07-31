import reflex as rx
from portfolio.components.icon_badge import icon_badge, icon_map, since_block
from portfolio.styles.style import FontSize as Size

def education(data) -> rx.Component:
    return rx.vstack(
        rx.heading(
            data.educationtitle,
            font_size=Size.H2.value,
        ),
        *[
            rx.flex(
                rx.hstack(
                    icon_badge(edu.icon),
                    rx.vstack(
                        rx.heading(
                            edu.title,
                            font_size=Size.H3.value,
                            color_scheme="gray",
                        ),
                        rx.text(
                            edu.description,
                        ),
                    ),
                    width="100%"
                ),
                since_block(edu.date,"map-pin",edu.place),
                flex_direction=["column-reverse", "row"],
                width="100%",
                gap = "var(--space-4);"
            )
            for edu in data.education
        ],

        width="100%",
        gap = "var(--space-6);"
    )