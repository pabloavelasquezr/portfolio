import reflex as rx
from enum import Enum

MAX_WIDTH = "880px"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css",
    "https://fonts.googleapis.com/css2?family=Inter:wght@100..900&family=Space+Mono:ital,wght@0,400;0,700;1,400;1,700&display=swap"
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
    },
    rx.heading: {
        "font-family": "var(--default-font-family)",
        "font-weight": "500",
        "line-height": "1.2",
        "margin-top": "0",
        "margin-bottom": "0.5em",
        "color": "var(--color-text)"
    },
    rx.avatar: {
        "-webkit-filter": "grayscale(100%)",
        "filter": "grayscale(100%)",
        "user-drag": "none",
        "-webkit-user-drag": "none",
        "user-select": "none",
        "-moz-user-select": "none",
        "-webkit-user-select": "none",
        "-ms-user-select": "none",
        "draggable": "false",
        # "pointer-events": "none"
    }
}

class FontSize(Enum):
    H1 = "1.714em"
    H2 = "1.429em"
    H3 = "1.143em"
    H4 = "1.071em"

class Color(Enum):
    BACKGROUND_LIGHT = '#f2f2f2"'
    BACKGROUND_DARK = '#1b1b1f'

class TextColor(Enum):
    LIGHT = '#444750'
    DARK = '#d9d9d9'
