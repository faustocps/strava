import flet as ft

def main(page: ft.Page):
    page.title = "faustocps"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Text("Olá, mundo!", size=24)
    )

ft.app(target=main)