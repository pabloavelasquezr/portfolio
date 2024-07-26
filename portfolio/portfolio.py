import reflex as rx
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
            # Skills
            skills(),
            # Experience
            experience(),
            # projects
            projects(),
            # Education
            education(),
            min_height="85vh",
            margin_top="50px",
        ),
        footer(),
        padding_top="0",
        background_color=rx.color_mode_cond(
            light="#f2f2f2", dark="#121212"
        ),
        color=rx.color_mode_cond(
            light="#444750", dark="#d9d9d9"
        ),
    )


app = rx.App(
    theme=rx.theme(
        appearance="light", accent_color="cyan"
    ),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap",
    ],
    style = {
        "--default-font-family": "--framer-font-family, Inter, Inter Placeholder, sans-serif",
        "-webkit-font-smoothing": "antialiased",
        "font-size": "14px",
    }
)
app.add_page(index)
