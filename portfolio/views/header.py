import reflex as rx
from portfolio.components.icon_badge import icon_map, icon_button
from portfolio.styles.style import TextColor
from portfolio.styles.style import FontSize as Size


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="pablo_avatar.jpg",
                size="6",
                _hover={
                    "-webkit-filter": "grayscale(0%)",
                    "filter": "grayscale(0%)",                    
                },
            ),
            rx.vstack(
                rx.heading(
                    "Pablo Velásquez",
                     font_size=Size.H1.value
                ),
                rx.text(
                    "Software Developer | Python | Systems Engineer | LMS | E-Learning"
                ),
                icon_map("map-pin"," Bucaramanga, Colombia"),
                rx.hstack(
                    icon_button("mail","Email","mailto:pabloavelasquez@gmail.com","pabloavelasquez@gmail.com"),
                    icon_button("file-text","Hoja de vida","/CV_pablo_velasquez_en.pdf"),
                    icon_button("github","GitHub","https://github.com/pabloavelasquezr"),
                    icon_button("linkedin","LinkedIn","https://www.linkedin.com/in/pabloavelasquez/"),
                    flex_wrap="wrap",
                ),
                align_items="start",

            ),
            
        )
    )