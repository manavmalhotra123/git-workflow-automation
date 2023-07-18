import time
import keyboard
from GitAutomation.git_handler import git_push, git_pull

def handle_shortcut(event):
    if event.name == 'l' and event.event_type == 'down':
        git_push()
    elif event.name == 'p' and event.event_type == 'down':
        git_pull()

# Register keyboard shortcuts
keyboard.on_press(handle_shortcut)

# Continuous loop
while True:
    time.sleep(1)  # Keep the script running
