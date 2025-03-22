# Crash: Auto Driving Car Simulation

## About Crash

Welcome to Crash. The car driving simulation program that lets you simulate what happens when you set cars in a tight grid, give them each a set of driving instructions and zero provisions for crash detection and prevention, and let the chips fall where they may!

The program is designed to work with a rectangular field, specified by its width and height. The bottom left coordinate of the field is at position (0,0), and the top right position is denoted (width,height). For example, a field with dimensions 10 x 10 would have its upper right coordinate at position (9,9).

One or more cars can be added to the field, each with a unique name, starting position, and direction they are facing. For instance, a car named "A" may be placed at position (1,2) and facing North.

A list of commands can be issued to each car, which can be one of three commands:

- L: rotates the car by 90 degrees to the left
- R: rotates the car by 90 degrees to the right
- F: moves forward by 1 grid point

If a car tries to move beyond the boundary of the field, the command is ignored, and the car stays in its current position. For example, if a car at position (0,0) is facing South and receives an F command, the command will be ignored as it would take the car beyond the boundary of the field.

## Getting started: Setup

_01 simulation setup_

```
Welcome to Auto Driving Car Simulation!

Please enter the width and height of the simulation field in x y format:
```

_02 exit_

```
Thank you for running the simulation. Goodbye!
```

_03 adding cars_


```
You have created a field of 10 x 10.

Please choose from the following options:
[1] Add a car to field
[2] Run simulation
```

_03.01 add car step 01 name a car_

```
Please enter the name of the car:
```

_03.02 add car step 02 initial pos and dir_

```
Please enter initial position of car A in x y Direction format:
```

_03.03 add car step 02 car commands_

```
Please enter the commands for car A:
```

only N, S, W, E (representing North, South, West, East) are allowed for direction.


```
Your current list of cars are:
- A, (1,2) N, FFRFFFFRRL

Please choose from the following options:
[1] Add a car to field
[2] Run simulation
```

## Run simulation

Then the system will run all car A's commands and all car B's commands, then respond with:

```
Your current list of cars are:
- A, (1,2) N, FFRFFFFRRL
- B, (7,8) W, FFLFFFFFFF

After simulation, the result is:
- A, collides with B at (5,4) at step 7
- B, collides with A at (5,4) at step 7

Please choose from the following options:
[1] Start over
[2] Exit
```

When processing commands for multiple cars, at every step, only one command can be processed for each car and it should be sequential.

Using the example above:
- At step 1, car A moves forward, and then car B moves forward.
- At step 2, car A moves forward, and then car B moves forward.
- At step 3, car A turn right, and then car B turns left.
- So on and so forth for the rest of the commands.

If some cars collide at certain step, then collided cars stop moving and no longer process further commands.

If cars do not have collision, then the system will print the final positions following example in Scenario 1.

## System requirements

To use the Crash program on your Windows PC you should have the following minimum requirement

 - Windows OS minimum 7 or higher
 - CPU 1 GHz
 - RAM 2 GB
 - Free disk memory:
      200 MB for python if not already installed
      100 MB for source code
 - Python version 3.9.0
 - network access to internet

## Installation and setup

1. __Install [Python 3.9](https://wiki.python.org/moin/BeginnersGuide/Download)__

If you have not already installed python 3.9, see the instructions on the website
Remember to check the box “Add Python 3.9 to PATH” during install

2. __(optional) Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)__

use Git to clone the source code onto your local pc, alternatively you can manually download the source code and unzip onto your local PC.

```
git clone https://github.com/taylorhickem/fpt_gic_auto_driving.git
cd fpt_gic_auto_driving
```

```
pip install -e .
```

The Crash program is now installed.

You can now interact with the program from the command line using the alias `crash` 

```
>crash start

Welcome to Auto Driving Car Simulation!

Please enter the width and height of the simulation field in x y format:
```
