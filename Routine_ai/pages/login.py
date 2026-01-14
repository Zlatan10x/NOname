from nicegui import ui

def page():
    @ui.page('/')
    def login_page():
        ui.label('Student Login').classes('text-2xl font-bold')

        student_id = ui.input('Student ID')
        password = ui.input('Password', password=True)

        ui.button('Login', on_click=lambda: ui.navigate.to('/upload'))
        ui.link('Not registered? Create an account', '/register')
