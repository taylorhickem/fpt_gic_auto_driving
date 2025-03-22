""" Crash: program entry point
"""
# dependencies ---------------------------------------------------------------
import sys


# constants ------------------------------------------------------------------
PROGRAM_NAME = 'Crash'
CLI_ALIAS = 'crash'
MESSAGES = {
    'program': {
        'welcome': f"Welcome to {PROGRAM_NAME}! Auto driving car simulation. To get started, select from any of these available commands: \n'{CLI_ALIAS} start': setup the simulation \n'{CLI_ALIAS} run': run the simulation\n'{CLI_ALIAS} test': run unit tests\n'{CLI_ALIAS} exit'\n ...",
        'start': f"Simulation setup.\n\nPlease enter the width and height of the simulation field in x y format:",
        'run': f"Running simulation...",
        'test': f"Running tests to verify that the program is installed correctly and works as expected ...",
        'exit': 'Exiting... Goodbye!'    
    }
}


# main -----------------------------------------------------------------------
def main():
    args = sys.argv[1:]
    program_prompts = MESSAGES.get('program', {})
    arg_program = args[0] if args else 'welcome'
    if arg_program in program_prompts:
        prompt = program_prompts.get(arg_program, '')
        print(prompt)
    else:
        print(f'ERROR. Unknown command: {arg_program}')
