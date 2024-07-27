import reflex as rx

def icon_badge(icon: str) -> rx.Component:
    return rx.hstack(
        rx.badge(
            rx.icon(icon,size=40),
            aspect_ratio="1",
            variant="soft",
        ),
    )

def icon_map(icon: str, text: str) -> rx.Component:
    return rx.badge(
        rx.icon(icon,size=15),
        text,
        display="inherit",color_scheme="gray"
    ),

def since_block(dates: str, icon="map-pin",text=" Bucaramanga, Colombia") -> rx.Component:
    return rx.vstack(
        rx.badge(
            dates,
        ),
        rx.badge(
            rx.icon(icon,size=15),
            text,
            display="inherit",color_scheme="gray"
        ),
        align_items="end",
        min_width="200px",
    ),
