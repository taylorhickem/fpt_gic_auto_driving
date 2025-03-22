""" Crash: program entry point
"""
# dependencies ---------------------------------------------------------------
import sys
import subprocess


# constants ------------------------------------------------------------------
PROGRAM_NAME = 'Crash'
CLI_ALIAS = 'crash'
MESSAGES = {
    'navigate': {
        'welcome': f"Welcome to {PROGRAM_NAME}! Auto driving car simulation. To get started, select from any of these available commands: \n'{CLI_ALIAS} start': setup the simulation \n'{CLI_ALIAS} run': run the simulation\n'{CLI_ALIAS} test': run unit tests\n'{CLI_ALIAS} exit'\n ...",
        'start': f"Simulation setup.\n\nPlease enter the width and height of the simulation field in x y format:",
        'run': f"Running simulation...",
        'test': f"Running tests to verify that the program is installed correctly and works as expected ...",
        'exit': 'Thank you for running the simulation. Goodbye!'    
    }
}


# main -----------------------------------------------------------------------
def prompt():
    args = sys.argv[1:]
    nav_prompts = MESSAGES.get('navigate', {})
    nav = args[0] if args else 'welcome'
    nav_args = args[1:] if len(args) > 1 else []
    prompt_msg = nav_prompts.get(nav, f'ERROR. Unknown command: {nav}')
    print(prompt_msg)
    return nav, nav_args


def navigate(command, args=[]):
    if command == 'start':
        print('Setup simulation: ## UNDER CONSTRUCTIONS##')
    elif command == 'test':
        subprocess.run(["pytest", "tests"])


def main():
    nav, nav_args = prompt()
    navigate(nav, args=nav_args)    
