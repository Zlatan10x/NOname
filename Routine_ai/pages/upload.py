from nicegui import ui
from components.navbar import navbar
from components.warnings import faculty_warning, slot_warning

def page():
    @ui.page('/upload')
    def upload_page():
        navbar()

        ui.label('Upload Course Data').classes('text-xl font-bold mt-4')

        ui.upload(
            label='Upload Course PDFs',
            multiple=True
        )

        ui.separator()

        ui.label('Preferences').classes('text-lg font-bold')

        ui.checkbox('Prefer specific faculties')
        faculty_warning()

        ui.checkbox('Prefer specific time slots')
        slot_warning()

        ui.button(
            'Generate AI Routines',
            on_click=lambda: ui.navigate.to('/suggestions')
        ).classes('mt-4')
