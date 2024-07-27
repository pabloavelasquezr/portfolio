import reflex as rx
from enum import Enum

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"
]

BASE_STYLE = {
    "--default-font-family": "--framer-font-family, Inter, Inter Placeholder, sans-serif",
    "-webkit-font-smoothing": "antialiased",
    "font-size": "14px",
    rx.button: {
        "--cursor-button": "pointer"
    },
    rx.badge: {
        "-webkit-user-select": "none",
        "user-select": "none"
    }
}

class Font(Enum):
    DEFAULT = "poppins"
    TITLE = "poppins"
    LOGO = "Space Mono"

class FontWeight(Enum):
    LIGHT = "300"
    MEDIUM = "500"

class Color(Enum):
    BACKGROUND_LIGHT = '#f2f2f2"'
    BACKGROUND_DARK = '#1b1b1f'

class TextColor(Enum):
    LIGHT = '#444750'
    DARK = '#d9d9d9'
