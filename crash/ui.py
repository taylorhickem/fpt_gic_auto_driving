# dependencies ---------------------------------------------------------------
import sys


# constants ------------------------------------------------------------------
PROGRAM_NAME = 'Crash'
CLI_ALIAS = 'crash'
MESSAGES = {
    'navigate': {
        'welcome': f"Welcome to {PROGRAM_NAME}! Auto driving car simulation.",
        'getting_started': f"To get started, select from any of these available commands: \n'start': setup the simulation \n'run': run the simulation\n'exit'\n ...",
        'start': f"Simulation setup.\n\nPlease enter the width and height of the simulation field in x y format:",
        'run': f"Running simulation...",
        'exit': 'Thank you for running the simulation. Goodbye!'    
    },
    'exceptions': {
        'invalid_input': 'ERROR. invalid input(s) {inputs}'
    }
}

# classes ------------------------------------------------------------------
class InteractiveApp:
    def __init__(self, input_fn=input, output_fn=print):
        self.input_fn = input_fn
        self.output_fn = output_fn

    def _exit(self):
        exit_msg = self._get_prompt(['navigate', 'exit'])
        self.output_fn(exit_msg)        

    def _exception_handle(self, ex_type='', params={}, msg='', action=''):
        msg_template = self._get_prompt(['exceptions', ex_type])
        if ex_type == 'invalid_input':
            inputs = params.get('inputs', [])
            msg = msg_template.format(inputs=inputs)
        if not action:
            action = 'exit'
        if msg:
            self.output_fn(msg)
        if action == 'exit':
            self._exit()

    def _get_prompt(self, levels, messages={}):
        prompt = ''
        key = levels[0] if levels else None
        if key:
            if not messages:
                messages = MESSAGES.copy()
            contents = messages.get(key, '')
            if isinstance(contents, dict):
                prompt = self._get_prompt(levels[1:], contents)
            else:
                prompt = contents
        return prompt

    def boot(self):
        welcome_msg = self._get_prompt(['navigate', 'welcome'])
        self.output_fn(welcome_msg)
        self._run()

    def _run(self):
        getting_started_msg = self._get_prompt(['navigate', 'getting_started'])
        nav = self.input_fn(getting_started_msg)
        nav_prompt = self._get_prompt(['navigate', nav])
        if nav_prompt:
            self.output_fn(nav_prompt)
            self.output_fn(f'executing {nav} ...')
        else:
            self._exception_handle(ex_type='invalid_input', params={'inputs':[nav]})
        
        #while True:
        #    answer = self.input_fn("Do you want to continue? (y/n): ")
        #    if answer.lower() == "n":
        #        self.output_fn("Goodbye!")
        #        break
        #    elif answer.lower() == "y":
        #        self.output_fn("Great! Let's continue...")
        #    else:
        #        self.output_fn("Please enter y or n.")