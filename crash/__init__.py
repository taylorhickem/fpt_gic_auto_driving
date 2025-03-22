""" Crash: program entry point
"""
# dependencies ---------------------------------------------------------------
import sys


# constants ------------------------------------------------------------------
PROGRAM_NAME = 'Crash'
CLI_ALIAS = 'crash'
MESSAGES = {
    'program': {
        'welcome': f"Welcome to {PROGRAM_NAME} CLI! Commands available: \n'{CLI_ALIAS} start'\n'{CLI_ALIAS} test'\n'{CLI_ALIAS} exit' \n ...",
        'start': f"Welcome to {PROGRAM_NAME}! Auto driving car simulation.\n\nPlease enter the width and height of the simulation field in x y format:",
        'test': f"Running tests to verify that the program is installed correctly and works as expected ...",
        'exit': 'Exiting... Goodbye!'    
    }
}


# main -----------------------------------------------------------------------
def main():
    args = sys.argv[1:]
    if not args:
        print(MESSAGES['welcome'])
    else:
        program_prompts = MESSAGES.get('program', {})
        arg_program = args[0]
        if arg_program in program_prompts:
            prompt = program_prompts.get(arg_program, '')
            print(prompt)
        else:
            print(f'ERROR. Unknown command: {arg_program}')
