import reflex as rx
from portfolio.components.icon_badge import icon_badge, icon_button, icon_stack_exp
from portfolio.styles.style import FontSize as Size

def projects(data) -> rx.Component:
    return rx.vstack(
        rx.heading(
            data.projectstitle,
            font_size=Size.H2.value,
        ),
        *[
            rx.flex(
                rx.hstack(
                    icon_badge(project.icon),
                    rx.vstack(
                        rx.heading(
                            project.title,
                            font_size=Size.H3.value,
                        ),
                        rx.text(
                            project.description,
                        ),
                        rx.hstack(
                            *[icon_stack_exp(tech.icon,tech.name) for tech in project.technologies],
                            flex_wrap="wrap",
                        ),
                        rx.hstack(
                            icon_button("link",project.tooltipurl,project.url),
                            icon_button("github",project.tooltipgithub,project.github),
                            flex_wrap="wrap",
                        ),
                    ),
                ),
                rx.vstack(
                    rx.card(
                        rx.image(
                            src=project.image,
                            border_radius="10px",
                        ),
                        width= "max-content",
                    ),
                    align_items="end",
                    min_width="334px"
                ),
                flex_direction=["column", "column", "row", "row", "row"],
                gap = "var(--space-3);"
            )
            for project in data.projects
        ],

        gap = "var(--space-6);"
    )