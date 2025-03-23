"""Crash program car simulation module
"""
# dependencies ---------------------------------------------------------------------
from . import state


# constants ------------------------------------------------------------------------


# classes --------------------------------------------------------------------------
class Case(object):
    grid = None
    cars = None
    def __init__(self, grid, cars):
        self.grid = grid
        self.cars = cars


class Grid(object):
    height = 0
    width = 0
    board = []
    status = 1
    error = ''
    def __init__(self, height, width):
        self.height = height
        self.width = width
        if self.valid():
            self._board_create()

    def _board_create(self):
        self.board = [[0 for j in range(self.width)] for i in range(self.height)]

    def dim(self):
        return {'height':self.height, 'width': self.width}

    def valid(self):
        return self.height > 0 and self.width > 0

    def valid_coordinates(self, i, j):
        h_valid = i >= 0 and i <= (self.height-1)
        w_valid = j >= 0 and j <= (self.width-1)
        coord_valid = h_valid and w_valid
        return coord_valid

    def add_car(self, car_id, i, j):        
        if self.slot_available(i, j):
            self.board[i][j] = car_id
            return 1
        else:
            self._exception_handle(
                ex_type='slot_unavailable', 
                params={'h': i, 'w': j, 'car_id': car_id},
                status=1
            )

    def _remove_car(self, i, j):
        self.board[i][j] = 0

    def move_car(self, car_id, pos_start, pos_new):
        i = pos_new[0]
        j = pos_new[j]
        if self.slot_available(i, j):
            self._remove_car(pos_start[0], pos_start[1])
            self.add_car(car_id, i, j)
            return 1
        else:
            self._exception_handle(
                ex_type='slot_unavailable', 
                params={'h': i, 'w': j, 'car_id': car_id},
                status=1
            )        

    def slot_available(self, i, j):
        if self.valid_coordinates(i, j):
            slot_index = self._get_slot_index(i, j)
            is_available = slot_index == 0
            return is_available
        else:
            self._exception_handle(
                ex_type='out_of_bounds',
                params={'h': i, 'w': j},
                status=1
            )

    def _get_slot_index(self, i, j):
        slot_index = self.board[i][j]
        return slot_index

    def status_reset(self):
        self.status = 1

    def _exception_handle(self, ex_type='', params={}, status=-1):
        error = ''
        if ex_type == 'out_of_bounds':
            h = params.get('h', None)
            w = params.get('w', None)
            error = f'ERROR. coordinates [{h}, {w}] outside of grid boundary {self.dim()}.'
        elif ex_type == 'slot_unavailable':
            h = params.get('h', None)
            w = params.get('w', None)
            car_id = params.get('car_id', None)
            error = f'ERROR. coordinate [{h}, {w}] is currently occupied by car_id:{car_id}.'
        self.status = self.status
        self.error = error


class Car(object):
    def __init__():
        pass


# main -----------------------------------------------------------------------------
def state_refresh():
    state.refresh()


def state_load():
    state.load()


def state_save():
    state.save()


def setup():
    print('Simulation setup: ## UNDER CONSTRUCTIONS##')
    response = {
        'success': 1
    }
    return response


def run():
    print('Simulation run: ## UNDER CONSTRUCTIONS##')
    response = {
        'success': 1
    }
    return response


def grid_create(**kwargs):
    print(f'Create grid: ## UNDER CONSTRUCTIONS## you passed {kwargs}')
    response = {
        'success': 1,
        'params': kwargs
    }
    return response


def car_add(**kwargs):
    print(f'Add car: ## UNDER CONSTRUCTIONS## you passed {kwargs}')
    response = {
        'success': 1
    }
    return response


def add(a, b):
    return a + b