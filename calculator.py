import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    num1 = ft.TextField(label="Número 1", width=120)
    num2 = ft.TextField(label="Número 2", width=120)
    basic_result = ft.Text("Respuesta: ", size=16)

    def calculate_basic(e):
        try:
            a = float(num1.value)
            b = float(num2.value)
            op = e.control.data

            if op == "+":
                res = a + b
            elif op == "-":
                res = a - b
            elif op == "x":
                res = a * b
            elif op == "dividir":
                res = a / b if b != 0 else "∞"

            basic_result.value = f"Respuesta: {res}"

        except ValueError:
            basic_result.value = "Ingresa números válidos"

        basic_result.update()

    basic_ops = ft.Row([
        ft.ElevatedButton("+", data="+", on_click=calculate_basic),
        ft.ElevatedButton("-", data="-", on_click=calculate_basic),
        ft.ElevatedButton("x", data="x", on_click=calculate_basic),
        ft.ElevatedButton("dividir", data="dividir", on_click=calculate_basic),
        ],
        spacing=10
    )

    basic_tab = ft.Column(
        [
            ft.Row([num1, num2], spacing=10),
            basic_ops,
            basic_result
        ],
        spacing=20
    )

    page.add(basic_tab)

ft.app(target=main)