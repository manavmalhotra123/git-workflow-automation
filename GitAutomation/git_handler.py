import time
import keyboard
from GitAutomation.git_handler import (
    git_init,
    git_clone,
    git_add,
    git_commit,
    git_push,
    git_pull,
    git_branch,
)

# Define the default keyboard shortcuts
DEFAULT_INIT_SHORTCUT = 'Ctrl+I'
DEFAULT_CLONE_SHORTCUT = 'Ctrl+C'
DEFAULT_ADD_SHORTCUT = 'Ctrl+A'
DEFAULT_COMMIT_SHORTCUT = 'Ctrl+M'
DEFAULT_PUSH_SHORTCUT = 'Ctrl+L'
DEFAULT_PULL_SHORTCUT = 'Ctrl+P'
DEFAULT_BRANCH_SHORTCUT = 'Ctrl+B'

def handle_shortcut(event):
    # Get the configured keyboard shortcuts (or use the defaults)
    init_shortcut = keyboard.get_hotkey_name(DEFAULT_INIT_SHORTCUT)
    clone_shortcut = keyboard.get_hotkey_name(DEFAULT_CLONE_SHORTCUT)
    add_shortcut = keyboard.get_hotkey_name(DEFAULT_ADD_SHORTCUT)
    commit_shortcut = keyboard.get_hotkey_name(DEFAULT_COMMIT_SHORTCUT)
    push_shortcut = keyboard.get_hotkey_name(DEFAULT_PUSH_SHORTCUT)
    pull_shortcut = keyboard.get_hotkey_name(DEFAULT_PULL_SHORTCUT)
    branch_shortcut = keyboard.get_hotkey_name(DEFAULT_BRANCH_SHORTCUT)

    # Check if the event matches the init shortcut
    if event.name == init_shortcut and event.event_type == 'down':
        git_init()

    # Check if the event matches the clone shortcut
    elif event.name == clone_shortcut and event.event_type == 'down':
        repository = input("Enter the repository URL to clone: ")
        git_clone(repository)

    # Check if the event matches the add shortcut
    elif event.name == add_shortcut and event.event_type == 'down':
        git_add()

    # Check if the event matches the commit shortcut
    elif event.name == commit_shortcut and event.event_type == 'down':
        message = input("Enter the commit message: ")
        git_commit(message)

    # Check if the event matches the push shortcut
    elif event.name == push_shortcut and event.event_type == 'down':
        git_push()

    # Check if the event matches the pull shortcut
    elif event.name == pull_shortcut and event.event_type == 'down':
        git_pull()

    # Check if the event matches the branch shortcut
    elif event.name == branch_shortcut and event.event_type == 'down':
        git_branch()

# Register keyboard shortcuts
keyboard.on_press(handle_shortcut)

# Continuous loop
while True:
    time.sleep(1)  # Keep the script running
