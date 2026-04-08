from taipy.gui import Gui

status = [
    ("warning", "Task is launched."),
    ("warning", "Tasks is waiting."),
    ("error", "Task timeout."),
    ("success", "Task Succeeded"),
    ("info", "Process was cancelled.")
]

# Info: svg icon (pants.svg)
# success: svg icon (hotel.svg)
# warning: svg icon (diving-goggles.svg)
# error: svg icon (hat.svg)
page = """
<|{status}|status|use_icon[info]=https://www.svgrepo.com/show/530594/pants.svg|use_icon[success]=https://www.svgrepo.com/show/530595/hotel.svg|use_icon[warning]=https://www.svgrepo.com/show/530596/diving-goggles.svg|use_icon[error]=https://www.svgrepo.com/show/530597/hat.svg|>
"""

if __name__ == "__main__":
  Gui(page).run(title="Status - With SVG icons")
