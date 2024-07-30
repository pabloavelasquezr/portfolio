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

def since_block(dates: str, icon,text) -> rx.Component:
    return rx.vstack(
        rx.badge(
            dates,
        ),
        rx.badge(
            rx.icon(icon,size=15),
            text,
            display="inherit",color_scheme="gray"
        ),
        align_items=["baseline","end"],
        min_width="200px",
    ),

def icon_stack(icon,text) -> rx.Component:
    return rx.badge(
        rx.box(
            class_name=icon,
        ),
        rx.text(text),
        size="5",
    ),

def icon_stack_exp(icon,text) -> rx.Component:
    return rx.badge(
        rx.box(
            class_name=icon,
        ),
        rx.text(text),
        size="3",
        color_scheme="gray"
    ),

def icon_button(icon,tooltiptext,link,text="") -> rx.Component:
    return rx.link(
        rx.tooltip(
            rx.button(rx.icon(icon),text,
                      variant= "surface" if text=="" else "solid"
                      ),
            content=tooltiptext,
        ),
        href=link,
        is_external=True
    ),
