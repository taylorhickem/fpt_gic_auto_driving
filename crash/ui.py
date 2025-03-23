""" Crash: program interactive user interface
"""

# dependencies ---------------------------------------------------------------
import sys
import re
from . import drive

# constants ------------------------------------------------------------------
PROGRAM_NAME = 'Crash'
CLI_ALIAS = 'crash'
DRIVE_METHODS = [
    'setup',
    'run',
    'grid_create',
    'car_add'
]
MESSAGES = {
    'navigate': {
        'welcome': f"Welcome to {PROGRAM_NAME}! Auto driving car simulation.",
        'getting_started': f"To get started, select from any of these available commands: \n'menu': return to this main menu\n'setup': setup the simulation \n'run': run the simulation\n'exit'\n ...",
        'setup': f"Simulation setup...",
        'run': f"Running simulation...",
        'exit': 'Thank you for running the simulation. Goodbye!',
        'menu': 'Returning to the main menu ...'    
    },
    'exceptions': {
        'invalid_input': 'ERROR. invalid input(s) {inputs}',
        'method_not_found': 'ERROR. method not found {method}',
        'fail': 'ERROR. something went wrong'
    },
    'grid_create': {
        'start': 'Create simulation grid ...',
        'input': 'Please enter the width and height of the simulation field in h, w format:',
        'success': 'created grid with height:{h} and width:{w}.',
        'fail': 'created grid unsuccessful.'
    },
    'car_add': {
        'start': 'Add car ...',
        'input': 'car name:',
        'success': 'car added:{name}.',
        'fail': 'add car unsuccessful.'
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
        self._menu()

    def _generic_drive_method(self, method):
        start_msg = self._get_prompt([method, 'start'])
        success_msg = self._get_prompt([method, 'success'])
        input_prompt = self._get_prompt([method, 'input'])
        fail_msg = self._get_prompt([method, 'fail'])
        result = 0
        if start_msg:
            self.output_fn(start_msg)
        if method in DRIVE_METHODS:
            drive_func = getattr(drive, method)            
            param_keys = re.findall(r'\{(.*?)\}', input_prompt)
            if input_prompt:
                input_response = self.input_fn(input_prompt)
                self.output_fn(f'this is what I received from you {input_response}')
                input_args = input_response.strip().split()
                self.output_fn(f'this is your response after I applied .strip().split() {input_args}')
                self.output_fn(f'I count {len(input_args)} arguments')
                if len(input_args) != len(param_keys):
                    self._exception_handle(ex_type='invalid_input', params={'inputs': input_response})
                    result = -1
                else:
                    prompt_kwargs = dict(zip(param_keys, input_args))
                    result = drive_func(**prompt_kwargs)
            else:
                result = drive_func()
        else:
            self._exception_handle(ex_type='method_not_found', params={'method': method})
            result = -1
        if result == 1:
            self.output_fn(success_msg)
        elif result == 0:
            self.output_fn(fail_msg)

    def _menu(self):
        menu_prompt = self._get_prompt(['navigate', 'getting_started'])
        nav = self.input_fn(menu_prompt)        
        if nav == 'exit':
            self._exit()
        elif nav == 'menu':
            transition_prompt = self._get_prompt(['navigate', nav])
            self.output_fn(transition_prompt)
            self._menu()
        elif nav == 'setup':
            self._setup()
        elif nav == 'run':
            self._run()
        else:
            self._exception_handle(ex_type='invalid_input', params={'inputs':[nav]})
        
    def _grid_create(self):
        self._generic_drive_method(method='grid_create')

    def _run(self):
        self._generic_drive_method(method='run')

    def _setup(self):
        self._grid_create()

        #while True:
        #    answer = self.input_fn("Do you want to continue? (y/n): ")
        #    if answer.lower() == "n":
        #        self.output_fn("Goodbye!")
        #        break
        #    elif answer.lower() == "y":
        #        self.output_fn("Great! Let's continue...")
        #    else:
        #        self.output_fn("Please enter y or n.")