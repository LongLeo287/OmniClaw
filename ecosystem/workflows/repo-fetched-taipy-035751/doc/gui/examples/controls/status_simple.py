from taipy.gui import Gui

status = [
    ("warning", "Task is launched."),
    ("warning", "Tasks is waiting."),
    ("error", "Task timeout."),
    ("success", "Task Succeeded"),
    ("info", "Process was cancelled.")
]

page = """
<|{status}|status|>
"""

if __name__ == "__main__":
  Gui(page).run(title="Status - Simple")
