from nicegui import ui
from components.navbar import navbar
from components.routine_card import routine_card
from state.mock_state import mock_state

def page():
    @ui.page('/suggestions')
    def suggestions_page():
        navbar()

        ui.label('AI Suggested Routines').classes('text-xl font-bold mt-4')

        def select_routine(routine_name):
            mock_state.selected_routine = routine_name

        routine_card(
            title='Best Routine',
            routine=[
                'Math - 9:00 AM',
                'Physics - 11:00 AM',
                'CS - 2:00 PM'
            ],
            on_select=lambda: select_routine('best')
        )

        routine_card(
            title='Second Best Routine',
            routine=[
                'Math - 10:00 AM',
                'Physics - 1:00 PM',
                'CS - 3:00 PM'
            ],
            on_select=lambda: select_routine('second')
        )

        ui.button(
            'Confirm Selection',
            on_click=lambda: ui.navigate.to('/edit')
        ).classes('mt-4')
