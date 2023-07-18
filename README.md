# Git Automation Project

This project provides an automation script for Git operations, allowing you to conveniently perform common tasks such as pushing and pulling changes. The script listens for keyboard shortcuts and executes the corresponding Git commands.

## Features

- Automatic Git push on specified keyboard shortcut (`Ctrl+L`)
- Automatic Git pull on specified keyboard shortcut (`Ctrl+P`)
- Continuous monitoring for uncommitted changes

## Prerequisites

- Python 3.x
- `keyboard` library (install using `pip install keyboard`)

## Getting Started

1. Clone or download this project to your local machine.

   ```bash
   git clone <https://github.com/manavmalhotra123/git-workflow-automation.git>


 pip install keyboard  

 python main.py & 

## Creating a new repository for your work 

mkdir my_work
cd my_work

1. Initialize a new Git repository
'''
 git init 

2. Customize and modify your project files within the new repository.

3. Configure the Git remote origin for your work repository by running the following command within the repository directory:

'''
git remote add origin <repository_url> 

Replace <repository_url> with the URL of your remote repository where you want to commit your work.

4.You are now ready to perform Git operations specific to your work repository. The automation script running in the background will not affect this repository.

# Stopping this automation 

To stop the automation script:

1. Press Ctrl+C in the terminal where the script is running.

2. The script will be terminated, and the automation functionality will cease.