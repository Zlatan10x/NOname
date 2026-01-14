from nicegui import ui

def routine_card(title, routine, on_select):
    with ui.card().classes('w-full mt-4'):
        ui.label(title).classes('font-bold')

        for item in routine:
            ui.label(f'• {item}')

        ui.button('Select This Routine', on_click=on_select)
