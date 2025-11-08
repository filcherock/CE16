import flet as ft

from ce16 import encode, decode

EMODE = True
DMODE = False

def main(page: ft.Page):
    page.title = "CE16 Client"
    page.window_width = 1200
    page.window_height = 800
    page.padding = 10
    page.theme_mode = ft.ThemeMode.DARK

    def handle_text_change(e):
        if EMODE == True:
            preview_area.value = encode(e.control.value)
        else:
            try:
                preview_area.value = decode(e.control.value)
            except ValueError:
                preview_area.value = "???"
        page.update()

    def encodeMode(e):
        global EMODE, DMODE
        EMODE = True
        DMODE = False
        modeLabel.value = "Mode: ENCODE"
    
    def decodeMode(e):
        global EMODE, DMODE
        EMODE = False
        DMODE = True
        modeLabel.value = "Mode: DECODE"

    input_field = ft.TextField(
        multiline=True,
        expand=True,
        min_lines=40,
        hint_text="Enter text...",
        border_color="transparent",
        on_change=handle_text_change,
    )

    modeLabel = ft.Text("Mode: ENCODE")
    button1 = ft.Button("Encode", style=ft.ButtonStyle(bgcolor=ft.Colors.TRANSPARENT), on_click=encodeMode)
    button2 = ft.Button("Decode", style=ft.ButtonStyle(bgcolor=ft.Colors.TRANSPARENT), on_click=decodeMode)
    btnrow = ft.Row(controls=[modeLabel, button1, button2], alignment=ft.MainAxisAlignment.CENTER)

    preview_area = ft.TextField(
        multiline=True,
        expand=True,
        read_only=True,
        min_lines=40,
        hint_text="",
        border_color="transparent",
    )


    page.add(input_field, btnrow, preview_area)
    page.update()

# Запуск приложения
if __name__ == "__main__":
    ft.app(target=main)