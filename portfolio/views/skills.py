import reflex as rx
from portfolio.styles.style import FontSize as Size

def skills(data) -> rx.Component:
    return rx.vstack(
        rx.heading(
            data.skillstitle,
            font_size=Size.H2.value,
        ),
        
        rx.list.unordered(
            *[rx.list.item(skill.skill) for skill in data.skills],
        ),
    )