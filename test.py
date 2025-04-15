import flet as ft
def main(page: ft.Page):
    # Componente Interativo
    container = ft.Container(
        content=ft.Text("Passe o mouse", size=20),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=10,
        animate=200,  # Animação suave
    )

    def on_hover(e):
        if e.data == "true":
            container.shadow = ft.BoxShadow(
                blur_radius=20,
                spread_radius=2,
                color=ft.colors.GREY_400,
            )
            container.bgcolor = ft.colors.BLUE_50
        else:
            container.shadow = None
            container.bgcolor = ft.colors.WHITE
        container.update()

    page.add(
        ft.GestureDetector(
            content=container,
            on_hover=on_hover,
            mouse_cursor=ft.MouseCursor.CLICK,
        )
    )

ft.app(target=main)