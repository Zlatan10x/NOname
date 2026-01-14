from nicegui import ui

def faculty_warning():
    ui.label(
        '⚠ Choosing faculty preferences may reduce routine optimization.'
    ).classes('text-yellow-600 text-sm')

def slot_warning():
    ui.label(
        '⚠ Choosing time slots may skip the best available faculties.'
    ).classes('text-yellow-600 text-sm')
