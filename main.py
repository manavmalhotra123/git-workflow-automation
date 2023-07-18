import time
import keyboard
from GitAutomation.git_handler import git_push, git_pull

# Define the default keyboard shortcuts
DEFAULT_PUSH_SHORTCUT = 'Ctrl+L'
DEFAULT_PULL_SHORTCUT = 'Ctrl+P'

def handle_shortcut(event):
    # Get the configured keyboard shortcuts (or use the defaults)
    push_shortcut = keyboard.get_hotkey_name(DEFAULT_PUSH_SHORTCUT)
    pull_shortcut = keyboard.get_hotkey_name(DEFAULT_PULL_SHORTCUT)

    # Check if the event matches the push shortcut
    if event.name == push_shortcut and event.event_type == 'down':
        git_push()

    # Check if the event matches the pull shortcut
    elif event.name == pull_shortcut and event.event_type == 'down':
        git_pull()

# Register keyboard shortcuts
keyboard.on_press(handle_shortcut)

# Continuous loop
while True:
    time.sleep(1)  # Keep the script running
