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
RESPONSE_TEMPLATE = {
    'success': -1,
    'params': {},
    'error': '',
    'msg': ''
}
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
        'input': 'Please enter the width and height of the simulation field in {h}, {w} format:',
        'success': 'created grid with height:{h} and width:{w}.',
        'fail': 'created grid unsuccessful.'
    },
    'cars_add': {
        'start': 'Add cars ...',
        'continue': '{add} another car? y/n.',
        'success': 'cars added:{names}.',
        'default': 'no cars added.',
        'fail': 'add cars unsuccessful.'
    },
    'car_add': {
        'start': 'Add a car ...',
        'success': 'car added:{name}.',
        'fail': 'add car unsuccessful.',
        'properties': [
            'name',
            'position',
            'direction',
            'moves'
        ],
        'name': {
            'input': '{name}:'
        },
        'position': {
            'input': 'position {x}, {y}:'
        },
        'direction': {
            'input': '{direction} [N, E, S, W]:'
        },
        'moves': {
            'input': '{moves}, a sequence of [L, R, F]:'
        }
    }
}


# classes ------------------------------------------------------------------
class InteractiveApp:
    def __init__(self, input_fn=input, output_fn=print):
        self.input_fn = input_fn
        drive.state_refresh()
        self.output_fn = output_fn

    def _exit(self):
        exit_msg = self._get_prompt(['navigate', 'exit'])
        self.output_fn(exit_msg)        

    def _exception_message(self, ex_type='', params={}, msg=''):
        if not ex_type:
            ex_type = 'fail'
        msg_template = self._get_prompt(['exceptions', ex_type])
        if ex_type == 'invalid_input':
            inputs = params.get('inputs', [])
            msg = msg_template.format(inputs=inputs) + f' {msg}' if msg else ''
        else:
            msg = msg_template + ' ' + f' {msg}' if msg else ''
        return msg

    def _exception_handle(self, ex_type='', params={}, msg='', action=''):
        ex_msg = self._exception_message(ex_type=ex_type, params=params, msg=msg)
        if not action:
            action = 'exit'
        if ex_msg:
            self.output_fn(ex_msg)
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

    def _get_input(self, levels):
        response = RESPONSE_TEMPLATE.copy()
        error = ''
        input_prompt = self._get_prompt(levels)
        if input_prompt:
            param_keys = re.findall(r'\{(.*?)\}', input_prompt)
            input_response = self.input_fn(input_prompt)
            input_args = input_response.strip().split()
            if len(input_args) == len(param_keys):
                prompt_kwargs = dict(zip(param_keys, input_args))
                response['success'] = 1
                response['params'] = prompt_kwargs
            else:
                ex_msg = f'number of args passed {len(input_args)} does not match expected {len(param_keys)}'
                error = self._exception_message(ex_type='invalid_input', params={'inputs': input_response}, msg=ex_msg)
        else:
            msg = f'no input prompt found for {levels}'
            response['success'] = 0
            response['msg'] = msg
        if error:
            response['success'] = -1
            response['error'] = error
        return response

    def _call_drive_method(self, method):
        response = RESPONSE_TEMPLATE.copy()
        error = ''
        start_msg = self._get_prompt([method, 'start'])
        if start_msg:
            self.output_fn(start_msg)
        if method in DRIVE_METHODS:
            drive_func = getattr(drive, method)
            inputs_response = self._get_input([method, 'input'])
            prompt_kwargs = {}
            if inputs_response['success'] == 1:
                prompt_kwargs = inputs_response.get('params', {})
            elif inputs_response['success'] == -1:
                error = inputs_response.get('error', 'unknown problem processing input')
            if prompt_kwargs:
                try:
                    response = drive_func(**prompt_kwargs)
                except Exception as e:
                    error = self._exception_message(ex_type='fail', msg=str(e))
            else:
                response = drive_func()
        else:
            error = self._exception_message(ex_type='method_not_found', params={'method': method})
        response['error'] = error
        return response

    def _generic_drive_method(self, method):
        start_msg = self._get_prompt([method, 'start'])
        if start_msg:
            self.output_fn(start_msg)
        if method in DRIVE_METHODS:
            drive_func = getattr(drive, method)
            inputs_response = self._get_input([method, 'input'])
            prompt_kwargs = {}
            if inputs_response['success'] == 1:
                prompt_kwargs = inputs_response.get('params', {})
            elif inputs_response['success'] == -1:
                ex_msg = inputs_response.get('error', 'unknown problem processing input')
                self._exception_handle(ex_type='invalid_input', msg=ex_msg, params={'inputs': ''})
            if prompt_kwargs:
                try:
                    response = drive_func(**prompt_kwargs)
                except Exception as e:
                    self._exception_handle(ex_type='fail', msg=str(e))
                else:
                    self._drive_response_process(method, response)
            else:
                response = drive_func()
                self._drive_response_process(method, response)
        else:
            self._exception_handle(ex_type='method_not_found', params={'method': method})

    def _drive_response_process(self, method, response):
        if response:
            outcome = response.get('success', -1)
            params = response.get('params', {})
            error = response.get('error', '')
            drive_msg = response.get('msg', '')
            if outcome == -1:
                self._exception_handle(msg=error)
            else:
                template_key = 'default'
                if outcome == 1:
                    template_key = 'success'
                msg_template = self._get_prompt([method, template_key])
                if params:
                    msg = msg_template.format(**params) + f' {drive_msg}' if drive_msg else ''
                else:
                    msg = msg_template + f' {drive_msg}' if drive_msg else ''
                self.output_fn(msg)

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
            self.run()
        else:
            self._exception_handle(ex_type='invalid_input', params={'inputs':[nav]})
        
    def _grid_create(self):
        self._generic_drive_method(method='grid_create')

    def _cars_add(self):
        method = 'cars_add'
        error = ''
        start_msg = self._get_prompt([method, 'start'])
        self.output_fn(start_msg)
        car_names = []
        add_open = True
        while add_open:
            add_response = self._car_add()
            outcome = add_response.get('success', -1)
            car_name = add_response.get('car_name', '')
            if outcome == 1:
                if car_name not in car_names:
                    car_names.append(car_name)
                    continue_response = self._get_input([method, 'continue'])
                    if continue_response['success'] == 1:                    
                        continue_yn = continue_response.get('params', {}).get('add', 'n')
                        add_open = continue_yn.lower() == 'y'
                    else:
                        add_open = False
                        outcome = -1
                        cnt_response_error = continue_response.get('error', '')
                        error = f'ERROR. problem interpreting response whether to continue adding more cars. {cnt_response_error}'
                else:
                    add_open = False
                    outcome = -1
                    error = f'ERROR. car name already exists {car_name}'
            else:
                add_error = add_response.get('error', '')
                error = f'ERROR. problem adding car {car_name}. {add_error}'
                add_open = False

        if outcome == -1:
            self._exception_handle(msg=error)
        else:
            response = {
                'success': outcome,
                'params': {'names': car_names},
            }
            self._drive_response_process(method, response)

    def _car_add(self):
        method = 'car_add'
        response = RESPONSE_TEMPLATE.copy()
        error = ''
        spec_success = -1
        start_msg = self._get_prompt([method, 'start'])
        self.output_fn(start_msg)
        car_properties = self._get_prompt([method, 'properties'])
        car_specs = {}
        if car_properties:
            spec_success = 1
            for prop in car_properties:
                prop_spec = {}
                spec_get = self._get_input([method, prop, 'input'])
                if spec_get['success'] == 1:
                    params_spec = spec_get.get('params', {})
                    if prop in params_spec:
                        prop_spec = params_spec[prop]
                    else:
                        prop_spec = params_spec
                    car_specs[prop] = prop_spec
                else:
                    spec_success = -1
                    error = spec_get.get('error', 'unknown problem processing input')
                    break
        else:
            error = self._exception_message(ex_type='method_not_found', params={'method':'car_properties'})

        if spec_success == 1:
            car_name = car_specs.get('name', '')
            try:
                drive_func = getattr(drive, method)
                response = drive_func(**car_specs)
            except Exception as e:
                error = f'ERROR. problem adding car {car_name}. {e}'
            response['car_name'] = car_name

        if error:
            response['error'] = error
        return response

    def run(self):
        # perform validation checks before running drive method 'run'
        self._generic_drive_method(method='run')

    def _setup(self):
        self._grid_create()
        self._cars_add()
