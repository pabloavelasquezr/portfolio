import reflex as rx
from portfolio.components.icon_badge import icon_map, icon_button
from portfolio.styles.style import FontSize as Size


def header(data) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.tooltip(    
                rx.avatar(
                    src=data.avatar,
                    size="6",
                    _hover={
                        "-webkit-filter": "grayscale(0%)",
                        "filter": "grayscale(0%)",
                    },
                ),
                content=data.greeting,
                align="start",
                align_offset=30,
            ),
            rx.vstack(
                rx.heading(
                    data.name,
                     font_size=Size.H1.value
                ),
                rx.text(
                    data.description,
                ),
                icon_map("map-pin",data.location),
                rx.hstack(
                    icon_button("mail","Email",f"mailto:{data.media.email}",data.media.email),
                    icon_button("file-text",data.media.tooltipcv,data.media.cv),
                    icon_button("github","GitHub",data.media.github),
                    icon_button("linkedin","LinkedIn",data.media.likedin),
                    flex_wrap="wrap",
                ),
                align_items="start",

            ),
            
        )
    )