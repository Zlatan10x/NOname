from nicegui import ui
from pages import login, reg, upload, sugg, routine_editor

def setup_routes():
    login.page()
    reg.page()
    upload.page()
    sugg.page()
    routine_editor.page()

setup_routes()
ui.run(title='AI Course Routine Builder')
