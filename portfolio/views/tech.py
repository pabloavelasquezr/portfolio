import reflex as rx
from portfolio.components.icon_badge import icon_stack_exp
from portfolio.styles.style import FontSize as Size

def tech(data) -> rx.Component:
    return rx.vstack(
        rx.heading(
            data.technologiestitle,
            font_size=Size.H2.value,
        ),
        rx.hstack(
            *[icon_stack_exp(tech.icon, tech.name) for tech in data.technologies],
            flex_wrap="wrap",
        )
    )