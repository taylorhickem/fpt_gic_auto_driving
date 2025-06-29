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