import subprocess

def git_push():
    try:
        subprocess.run(['git', 'add', '.'])  # Add all changes to the staging area
        subprocess.run(['git', 'commit', '-m', 'Automated commit'])  # Commit the changes
        subprocess.run(['git', 'push'])  # Push the changes to the remote repository
        print("Git push successful!")
    except Exception as e:
        print(f"An error occurred: {e}")

def git_pull():
    try:
        subprocess.run(['git', 'pull'])  # Pull the latest changes from the remote repository
        print("Git pull successful!")
    except Exception as e:
        print(f"An error occurred: {e}")
