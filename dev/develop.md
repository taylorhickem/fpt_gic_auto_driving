## Development strategy

| id | status| stage |
| - | - | - |
| 01 | closed | design |
| 02 | closed | tests |
| 03 | closed | ui |
| 04 | closed | setup |
| 05 | open | simulation |

## 01. (closed) design

- system architecture
- flowchart
- test cases

# 02. (closed) tests

- create entry point ui
- create pytest test.py and test entry point
- run tests expected to fail

# 03. (closed) ui

- cli user interface, walks through basic flowchart 
- input validation, exception handling

# 04. (closed) setup

- setup a simulation
 - create grid
 - add cars
- separate model from ui
- handle state as *.json

# 05. (open) simulation

 - run simulation
    - step through moves sequentially
    - reposition the cars
    - detect and handle exceptions
        - collisions
        - boundary


## Session logs

Session logs are recorded in reverse-chronological order and timestamped to Singapore timezone. Earlier entries are at the top and older entries are at the bottom.

### Linear algebra model [Developer] review and develop 2025-06-29 22:18

review
 - added ui navigation and retries
 - tested simple simulation validated generated response and ran without exception
   - one case by coincidence detected a collision, but I didn't verify wether that case SHOULD have had a collision

### Linear algebra model [Codex] Codex prompt 2025-06-29 20:47

- Implemented linear algebra helper functions `case_to_matrix`, `matrix_to_case`
  and `linear_step` in `drive.py`.
- Completed `run` method to execute simulation steps and persist `state.json`.
- Added constants for direction vectors and fixed a bug in `Grid.car_move`.
- Extended tests to cover car add and simulation run; all tests passing.
- Documented matrix translation workflow in `docs/design.md`.


### Linear algebra model [Developer] Codex prompt 2025-06-29 20:30

For context about the app, refer to `README.md` and `/docs`.  Refer to `/docs/design.md` for details about the linear model. Refer to `/dev` and specifically the dev note `/dev/develop.md` for notes about current status of the development of the app. 

the situation
`Crash` is a python command line application that simulates a set of integer car moves in a grid and checks for conditions whether they collided or reached the boundary of the grid.  The UI and basic object model are mostly complete, and what remains is to implement the simulation.  

your task
- review the current implementation and design, app architecture, modules, ui control flow, classes, methods
- complete the program and develop the simulation
- add test cases to `test.py` for ui grid create, cars add and simulation run
- validate your implementation by testing using `test.py` and resolve issues as required
- complete the ui to run the simulation, guide the user with feedback notifications, output simulation results, and add retries and navigation menus where they are missing
    - use the existing `ui.py` methods such as output_fn() for basic navigation, setting up, starting, exiting simulation, you are free to use print() when you are inside the simulation with intermediate updates during a simulation run, such as detecting exception conditions for collision and boundary violations
- implement the linear model method, including the ORM-linear model translations
- implement methods to persist the state `state.json` between each simulation move
- update the documentation where you have added more details not already convered 
- record your observations and activity during your session in the ## Session logs section of the dev note in the section ### Linear algebra model [Codex] Codex prompt 2025-06-29 <HH>:<MM>.
- create a PR with your updates in the source code, `/docs` and session log
