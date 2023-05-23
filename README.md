# Project: turing_machine
Python project, which implements and simulates a simple Turing machine.

## Basics of Turing machines
As you might know, a Turing machine is a 7-tuple:
  - it needs to have a *set of states*,
  - a *starting state*,
  - at least one *end state*.
  - It also consists of a *input-alphabet* which is a subset of the...
  - ...*tape-alphabet*, on which the machine operates.
  - Furthermore, the special *blank-symbol* is needed and...
  - ...finally a *delta-/transition-function*, of course.

More information about the basics of Turing machines can be found in several books or online.\
\
My intention was to create a simple yet functional little Turing machine simulator.\
The idea came to me, when we had to create a Turing machine in order to solve our lecture's exercises at university.\
I did not feel like doing it on paper, so I created this project and\
solved the task in a more practical way (not often seen in theoretical computer science). :-)\
I wanted to share my project to demonstrate the workings of Turing machines more vivid, since it has a deeply theoretical background\
and is not always as easy to understand as other topics in computer science.

## Content
The project contains several files. Let us briefly look at the "**Exceptions**"-folder, which contains several\
exception classes. As they are not the most interesting thing about this project, let us skip them.

The heart of the project is "**TuringMachine.py**", which implements a fully functional Turing machine.\
If you want to simulate a Turing machine, the script "**TuringSimulator.py**" comes in handy. This class creates\
a new Turing machine for you and initialises the simulation.\
However, to make the Turing machine work correctly, the right transition-function has to be used.\
If you take a look at "**turing.py**", you will find a script which implements the machine's functionality.\
Every attribute the machine has will be set here.\
A fully functional attribute-set to make the machine add two binary numbers is ready-to-use and you can find it\
in "**add.turing**".

## How to use
Before the simulation can start, the right attributes have to be set.
Here's a quick overview of this must be done:
  - Specifiy the alphabet, the machine should operate on. In this case, the input- and the tape-alphabet are merged into one single alphabet.
    This alphabet is represented by a Python-list and may only contain symbols represented by strings.
  - Define the input-state, a list of ending-states and add additional "normal" states. Every state must be represented by a string.
  - Set the machines' blank-symbol and define the number of tapes your machine should have.
  - If the machine should print the action it's going to do, set the print_actions-attribute to True, else False. The machine prints it's configuration
    (it's tapes) after every step by default.
  - Finally implement your delta-function. It's represented by a dictionary, where the keys are tuples and are\
    composed by the current state and the symbols on the tapes.\
    The corresponding values contain the successive state, the symbols to write on the tapes and the moves, which the write-and-read-unit(s) should do.\
    The format is as follows: delta = {\
    tuple(current_state, tuple(symbol_tape_1, ..., symbol_tape_n)): \
    tuple(succ_state, tuple(to_write_1, ..., to_write_n), tuple(move_1, ..., move_n)),\
    ...}.\
You can find another detailed description inside the scripts.

## Contact
If you liked this project or have any comments, feel free to contact me:\
\
Simon Schulze\
simon.schulze@s2021.tu-chemnitz.de\
Technische Universitaet Chemnitz/Chemnitz University of Technology
