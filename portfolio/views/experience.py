import reflex as rx
from portfolio.components.icon_badge import icon_badge, since_block
from portfolio.styles.style import FontSize as Size

def experience(data) -> rx.Component:
    return rx.vstack(
        rx.heading(
            data.experiencetitle,
            font_size=Size.H2.value,
        ),
        *[
            rx.flex(
                rx.hstack(
                    icon_badge(exp.icon),
                    rx.vstack(
                        rx.heading(
                            exp.title,
                            font_size=Size.H3.value,
                        ),
                        rx.heading(
                            exp.subtitle,
                            font_size=Size.H4.value,
                            color_scheme="gray",
                        ),
                        rx.list.unordered(
                            *[rx.list.item(item.item) for item in exp.description],
                        ),
                    )
                ),
                since_block(exp.date,"map-pin",exp.place),
                flex_direction=["column-reverse", "row"],
                gap = "var(--space-3);"
            )
            for exp in data.experience
        ],

        gap = "var(--space-6);"
    )