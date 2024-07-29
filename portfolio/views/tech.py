import reflex as rx
from portfolio.components.icon_badge import icon_stack_exp

def tech() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Tecnologías",
            font_size="1.5rem",
        ),
        rx.text(
            "Estas son las tecnologías que he utilizado en mis proyectos:",
        ),
        rx.hstack(
            icon_stack_exp("devicon-python-plain","Python"),
            icon_stack_exp("devicon-django-plain","Django"),
            icon_stack_exp("devicon-javascript-plain","JavaScript"),
            icon_stack_exp("devicon-react-original","React"),
            icon_stack_exp("devicon-postgresql-plain","PostgreSQL"),
            icon_stack_exp("devicon-mysql-plain","MySQL"),
            icon_stack_exp("devicon-html5-plain","HTML5"),
            icon_stack_exp("devicon-css3-plain","CSS3"),
            icon_stack_exp("devicon-bootstrap-plain","Bootstrap"),
            icon_stack_exp("devicon-git-plain","Git"),
            icon_stack_exp("devicon-github-original","GitHub"),
            icon_stack_exp("devicon-vscode-plain","VS Code"),
            icon_stack_exp("devicon-figma-plain","Figma"),
            flex_wrap="wrap",
        )
    )