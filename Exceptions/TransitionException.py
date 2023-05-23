class TransitionException(LookupError):
    def __init__(self, transition):
        self.transition = transition

    def __str__(self):
        return f"""No such transition found: {self.transition}.
        Please check your transitions!"""
