from nicegui import ui

def dropdown_row(course, times):
    with ui.row():
        ui.label(course)
        ui.select(times, value=times[0])
