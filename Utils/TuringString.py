# TODO add joker symbol (not implemented yet)

class TuringString(str):

    """
    Class to imitate the joker symbol to match all symbols.
    """

    def __eq__(self, other):
        return str(self).__eq__(str(other)) or str(other).__eq__("*")
