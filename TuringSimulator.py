import turing
from TuringMachine import TuringMachine


class TuringSimulator:
    def __init__(self) -> None:
        self.machine = TuringMachine(turing.alphabet, turing.init_state, turing.states,
                                     turing.end_states, turing.delta, blank=turing.blank,
                                     tapes=turing.tapes, print_actions=turing.print_actions)

    def simulate(self, word: str, speed: float) -> None:
        self.machine.simulate(word, speed)


if __name__ == "__main__":
    ts = TuringSimulator()
    ts.simulate("11100#1101", 4)
