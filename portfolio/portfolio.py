import reflex as rx
from portfolio.styles.style import STYLESHEETS, BASE_STYLE, Color, TextColor
from portfolio.components.navbar import navbar
from portfolio.views.header import header
from portfolio.views.about import about
from portfolio.views.skills import skills
from portfolio.views.experience import experience
from portfolio.views.education import education
from portfolio.views.projects import projects
from portfolio.views.footer import footer

class State(rx.State):
    pass


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        navbar(),
        
        rx.vstack(
            header(),
            about(),
            rx.divider(),
            skills(),
            rx.divider(),
            experience(),
            rx.divider(),
            projects(),
            rx.divider(),
            education(),
            min_height="85vh",
            margin_top="50px",
        ),
        footer(),
        padding_top="0",
        background_color=rx.color_mode_cond(
            light=Color.BACKGROUND_LIGHT.value, 
            dark=Color.BACKGROUND_DARK.value
        ),
        color=rx.color_mode_cond(
            light=TextColor.LIGHT.value, 
            dark=TextColor.DARK.value
        ),
    )


app = rx.App(
    theme=rx.theme(
        radius="full", accent_color="cyan"
    ),
    stylesheets = STYLESHEETS,
    style = BASE_STYLE
)
app.add_page(index)
