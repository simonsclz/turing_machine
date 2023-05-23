from __future__ import annotations
from time import sleep
from Turing.Exceptions.TransitionException import TransitionException
from Turing.Exceptions.MoveException import MoveException


class TuringMachine:
    """
    Class to simulate a Turing machine.
    """

    def __init__(self, alphabet: list, init_state: str, states: list,
                 end_states: list, delta: dict, blank: str = ' ', tapes: int = 1,
                 print_actions: bool = False) -> None:

        """
        Constructor of Turing machine.
        :param alphabet: Specifies the alphabet the machine should use.
                Should be a list of form: [symbol_1, ..., symbol_n] where
                each symbol is a string.
        :param init_state: Specifies the initial state of the machine.
                Should be of type string.
        :param states: Specifies the normal states the machine should have.
                Should be a list of form: [state_1, ..., state_n] where each
                state is represented as a string.
        :param end_states: Specifies the end states of the machine.
                Should be a list of form: [end_state_1, ..., end_state_n] where each
                end state is represented as a string.
        :param delta: Specifies the transition function of the machine.
                Should be a dictionary of form: {[state, symbol]:
                [successive_state, symbol_to_write, move], ...} where move
                is either 'l' (left), 'r' (right) or 'n' (neutral).
                Each state has to be of type string.
                Each state, each symbol to write and each move has to be a tuple of strings.
                The size of the tuple depends on the number of tapes.
        :param blank: The blank symbol of the machine. Has to be a string.
                Standard is ' '.
        :param tapes: Number of tapes the machine will have. Has to be a string.
                Standard is 1.
        :param print_actions: Enables or disables the machine's feature to print
                each move's details (which direction, symbol to write).
        """

        self.alphabet = alphabet
        self.init_state = init_state
        self.states = states
        self.end_states = end_states
        self.delta = delta
        self.blank = blank
        self.tapes = [[] for _ in range(tapes)]
        self.amount_tapes = tapes
        self.print_actions = print_actions

    def __move_left(self, word: list, index: int, symbol_to_write: str) -> tuple:

        """
        Moves the write-and-read-unit of the machine one square to the left.
        :param word: The word, on which the machine is simulated on.
                Has to be a list of strings (symbols).
        :param index: The current index the machine points on.
        :param symbol_to_write: The symbol to write on the current position.
        :return: The updated word and index as a tuple.
        """

        if self.print_actions:
            print(f"move l, symbol {word[index]}->{symbol_to_write}")

        word[index] = symbol_to_write
        if index == 0:
            word.insert(0, self.blank)
            index = 0
        else:
            index -= 1
        return word, index

    def __move_right(self, word: list, index: int, symbol_to_write: str) -> tuple:

        """
        Moves the write-and-read-unit of the machine one square to the right.
        :param word: The word, on which the machine is simulated on.
                Has to be a list of strings (symbols).
        :param index: The current index the machine points on.
        :param symbol_to_write: The symbol to write on the current position.
        :return: The updated word and index as a tuple.
        """

        if self.print_actions:
            print(f"move r, symbol {word[index]}->{symbol_to_write}")

        word[index] = symbol_to_write
        if index == len(word) - 1:
            word.append(self.blank)
            index = len(word) - 1
        else:
            index += 1
        return word, index

    def __move_neutral(self, word: list, index: int, symbol_to_write: str) -> list:

        """
        Does not move the write-and-read-unit of the machine, updates the symbol, if necessary.
        :param word: The word, on which the machine is simulated on.
                Has to be a list of strings (symbols).
        :param index: The current index the machine points on.
        :param symbol_to_write: The symbol to write on the current position.
        :return: The updated word and index as a tuple.
        """

        if self.print_actions:
            print(f"move n, symbol {word[index]}->{symbol_to_write}")

        word[index] = symbol_to_write
        return word

    def __print_configuration(self, indices: list) -> None:

        """
        Prints the current configuration of the machine.
        :param indices: List of indices where the write-and-read-units on each tape point to.
        :return: Nothing. Prints the configuration on the screen.
        """

        for tape_index in range(self.amount_tapes):
            # print(f"Tape {tape_index+1}:")
            tape = self.tapes[tape_index]
            for index in range(len(tape)):
                if index == indices[tape_index]:
                    # prints the current index bold
                    print(">" + tape[index] + "<", end="\t")
                else:
                    print(tape[index], end="\t")
            print("")
        print("\n***\n")

    def simulate(self, word: str, speed: float) -> None:

        """
        This method does the simulation of the machine.
        :param word: The word to simulate the Turing machine on.
                Has to be of type string.
                Initially, the write-and-read-unit of the machine points
                to the first symbol of the word.
        :param speed: Specifies the speed of the simulation.
                Has to be a float.
        :return: Nothing. Prints the simulation on the screen.
        """

        current_state = self.init_state
        word = list(word)
        for tape_index in range(self.amount_tapes):
            if tape_index == 0:
                self.tapes[0] = word
            else:
                self.tapes[tape_index] = [self.blank] * len(word)
        indices = [0 for _ in range(self.amount_tapes)]

        # loop while the machine is not in an end state

        while current_state not in self.end_states:
            # print the current config
            self.__print_configuration(indices)

            # select the index-th tape and find the current symbol
            symbol = tuple([self.tapes[index][indices[index]] for index in range(self.amount_tapes)])
            if (current_state, symbol) in self.delta.keys():
                successive_state, symbol_to_write, move = self.delta[(current_state, symbol)]
                for tape_index in range(self.amount_tapes):

                    # only if action-printing is desired
                    # all other details (direction, symbols) are implemented in the move-functions
                    if self.print_actions:
                        print(f"Tape {tape_index + 1}:", end=" ")

                    if move[tape_index] == 'l':
                        self.tapes[tape_index], indices[tape_index] = \
                            self.__move_left(self.tapes[tape_index], indices[tape_index],
                                             symbol_to_write[tape_index])
                    elif move[tape_index] == 'r':
                        self.tapes[tape_index], indices[tape_index] = \
                            self.__move_right(self.tapes[tape_index], indices[tape_index],
                                              symbol_to_write[tape_index])
                    elif move[tape_index] == 'n':
                        self.tapes[tape_index] = \
                            self.__move_neutral(self.tapes[tape_index], indices[tape_index],
                                                symbol_to_write[tape_index])
                    else:
                        raise MoveException(move)

                # update the state
                current_state = successive_state
                sleep(speed)

            else:
                raise TransitionException((current_state, symbol))
        else:
            # print last config
            self.__print_configuration(indices)
            print("Successfully accepted!")
