from nicegui import ui

def navbar():
    with ui.row().classes('w-full justify-between p-4 border-b'):
        ui.label('AI Course Routine Builder').classes('font-bold')
        ui.button('Logout', on_click=lambda: ui.navigate.to('/'))
