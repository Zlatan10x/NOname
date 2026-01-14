from nicegui import ui
from components.navbar import navbar
from components.dropdown_row import dropdown_row
from state.mock_state import mock_state

def page():
    @ui.page('/edit')
    def editor_page():
        navbar()

        ui.label('Modify Your Routine').classes('text-xl font-bold mt-4')

        ui.label(f'Selected Routine: {mock_state.selected_routine}')

        dropdown_row('Math', ['9:00 AM', '10:00 AM'])
        dropdown_row('Physics', ['11:00 AM', '1:00 PM'])
        dropdown_row('CS', ['2:00 PM', '3:00 PM'])

        ui.button('Save Final Routine').classes('mt-4')
