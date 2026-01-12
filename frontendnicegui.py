from nicegui import ui

# =====================================================
# GLOBAL APP STATE (BACKEND WILL CONTROL THESE)
# =====================================================
current_page = 1  # 1=Upload, 2=Analysis, 3=Results

uploaded_files = {
    'courses.pdf': False,
    'faculty.csv': False,
    'timeslots.csv': False,
    'exams.csv': False,
}

analysis_steps = [
    'Reading files',
    'Processing courses',
    'Analyzing constraints',
    'Checking conflicts',
    'Generating schedules',
]
completed_steps = 0  # backend updates this

results_data = [
    {
        'id': 1,
        'title': 'Option 1',
        'color': 'blue',
        'courses': ['Database', 'AI Ethics', 'Networks'],
        'conflicts': 0,
        'free_days': 3,
        'favorite': True,
    },
    {
        'id': 2,
        'title': 'Option 2',
        'color': 'purple',
        'courses': ['ML', 'Web Dev', 'Cloud'],
        'conflicts': 0,
        'free_days': 3,
        'favorite': False,
    },
]

# =====================================================
# BACKEND HOOKS (TEAM WILL REPLACE LOGIC HERE)
# =====================================================
def handle_upload(e):
    """BACKEND: save file, validate, mark uploaded"""
    name = e.file.name
    if name in uploaded_files:
        uploaded_files[name] = True

    # Auto-move to analysis when required files uploaded
    if all(uploaded_files.values()):
        go_to_page(2)

    ui.refresh()


def backend_update_analysis(step_count: int):
    """BACKEND: call this when AI progresses"""
    global completed_steps
    completed_steps = step_count
    if completed_steps >= len(analysis_steps):
        go_to_page(3)
    ui.refresh()


def toggle_favorite(option_id: int):
    """OPTIONAL BACKEND: persist favorite"""
    for r in results_data:
        if r['id'] == option_id:
            r['favorite'] = not r['favorite']
    ui.refresh()


def go_to_page(page: int):
    global current_page
    current_page = page
    ui.refresh()

# =====================================================
# STYLING
# =====================================================
ui.add_head_html("""
<style>
body {
    margin: 0;
    background: #f5f9ff;
}
.page {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}
.upload-box {
    border: 2px solid #93c5fd;
    border-radius: 16px;
    padding: 32px;
}
.file-row {
    background: #ecfdf5;
    border: 1px solid #bbf7d0;
    border-radius: 10px;
    padding: 10px 14px;
}
.file-row.disabled {
    background: #f8fafc;
    border-color: #e5e7eb;
    color: #9ca3af;
}
.option-card {
    border-radius: 16px;
    overflow: hidden;
}
.option-header {
    padding: 10px 14px;
    color: white;
    font-weight: 600;
    display: flex;
    justify-content: space-between;
}
</style>
""")

# =====================================================
# UI RENDERER
# =====================================================
@ui.refreshable
def render():

    # =================================================
    # PAGE 1 — UPLOAD
    # =================================================
    if current_page == 1:
        with ui.element('div').classes('page'):
            with ui.card().classes('w-[420px] p-6'):

                with ui.row().classes('items-center gap-2 mb-4'):
                    ui.label('1').classes(
                        'bg-blue-600 text-white rounded-full w-6 h-6 flex items-center justify-center'
                    )
                    ui.label('Upload Data').classes('text-blue-600 font-semibold')

                with ui.column().classes('upload-box items-center gap-3'):
                    ui.icon('upload').classes('text-5xl text-blue-400')
                    ui.label('Upload CSV Files').classes('text-lg font-medium')

                    ui.upload(
                        on_upload=handle_upload,
                        auto_upload=True
                    ).props('accept=.csv,.pdf').classes('hidden')

                    ui.button(
                        'Browse Files',
                        on_click=lambda: ui.run_javascript(
                            "document.querySelector('input[type=file]').click()"
                        )
                    ).classes('bg-blue-600 text-white px-6')

                with ui.column().classes('mt-5 gap-2'):
                    for name, done in uploaded_files.items():
                        cls = 'file-row' if done else 'file-row disabled'
                        with ui.row().classes(f'items-center justify-between {cls}'):
                            ui.label(name)
                            if done:
                                ui.icon('check_circle').classes('text-green-500')

    # =================================================
    # PAGE 2 — AI ANALYSIS (READ ONLY)
    # =================================================
    if current_page == 2:
        progress = completed_steps / len(analysis_steps)

        with ui.element('div').classes('page'):
            with ui.card().classes('w-[420px] p-8'):

                with ui.row().classes('items-center gap-2 mb-6'):
                    ui.label('2').classes(
                        'bg-purple-600 text-white rounded-full w-6 h-6 flex items-center justify-center'
                    )
                    ui.label('AI Analysis').classes('text-purple-600 font-semibold')

                ui.icon('psychology').classes('text-7xl text-purple-500 mx-auto')
                ui.label('Processing Data...').classes('text-center mt-4')

                with ui.column().classes('mt-6 gap-3'):
                    for i, step in enumerate(analysis_steps):
                        done = i < completed_steps
                        with ui.row().classes('items-center gap-3'):
                            ui.icon(
                                'check_circle' if done else 'check_circle'
                            ).classes(
                                'text-green-500' if done else 'text-gray-300'
                            )
                            ui.label(step)

                ui.linear_progress(progress).classes('mt-8')
                ui.label(
                    f'{int(progress * 100)}% Complete'
                ).classes('text-center text-sm text-gray-500 mt-2')

    # =================================================
    # PAGE 3 — RESULTS
    # =================================================
    if current_page == 3:
        with ui.element('div').classes('page'):
            with ui.card().classes('w-[480px] p-6'):

                ui.label(
                    f'{len(results_data)} Optimized Schedules Generated'
                ).classes('text-center text-gray-600 font-medium mb-4')

                for r in results_data:
                    header_color = 'bg-blue-500' if r['color'] == 'blue' else 'bg-purple-500'

                    with ui.card().classes('option-card mb-5'):
                        with ui.row().classes(f'option-header {header_color}'):
                            with ui.row().classes('items-center gap-2'):
                                ui.icon('calendar_today')
                                ui.label(r['title'])

                            ui.icon(
                                'star' if r['favorite'] else 'star_border'
                            ).classes(
                                'cursor-pointer text-yellow-300'
                            ).on(
                                'click',
                                lambda e, oid=r['id']: toggle_favorite(oid)
                            )

                        with ui.column().classes('p-4 gap-3'):
                            with ui.row().classes('gap-2 flex-wrap'):
                                for c in r['courses']:
                                    ui.chip(c).props('outline')

                            with ui.row().classes('gap-3'):
                                ui.badge(f"{r['conflicts']} Conflicts", color='green')
                                ui.badge(f"{r['free_days']} Free Days", color='blue')


render()
ui.run()