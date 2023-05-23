class MoveException(LookupError):
    def __init__(self, move):
        self.move = move

    def __str__(self):
        return f"""{self.move} is not an allowed move.
        Please use a tuple consisting of either 'r' (right), 'l' (left) or 'n' (neutral)
        and make sure, the size of the tuple matches the machine's amount of tapes!"""
