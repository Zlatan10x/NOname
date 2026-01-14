from nicegui import ui

from nicegui import ui

def page():
    @ui.page('/register')
    def register_page():
        ui.label('Register').classes('text-2xl font-bold')

        ui.input('Student ID')
        ui.input('Password', password=True)
        ui.input('Confirm Password', password=True)

        ui.button('Register', on_click=lambda: ui.navigate.to('/'))
