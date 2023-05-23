# The alphabet, the machine should work on
alphabet = ["1", "0", "#"]

# Initial state
init_state = "z_0"

# End states
end_states = ["z_end"]

# All states, add "normal" states
states = [init_state] + end_states + ["z_1", "z_2", "z_3", "z_add", "z_carry"]

# The blank
blank = "⃞"

# Number of tapes
tapes = 3

# If the machine should print its actions
print_actions = True

# Delta-/transition-function
delta = {
    ("z_0", ("0", blank, blank)): ("z_0", ("0", blank, blank), ("r", "r", "r")),
    ("z_0", ("1", blank, blank)): ("z_0", ("1", blank, blank), ("r", "r", "r")),
    ("z_0", ("#", blank, blank)): ("z_1", ("#", blank, blank), ("r", "l", "l")),

    ("z_1", ("0", blank, blank)): ("z_1", ("0", blank, blank), ("r", "n", "n")),
    ("z_1", ("1", blank, blank)): ("z_1", ("1", blank, blank), ("r", "n", "n")),
    ("z_1", (blank, blank, blank)): ("z_2", (blank, blank, blank), ("l", "n", "n")),

    ("z_2", ("0", blank, blank)): ("z_2", (blank, "0", blank), ("l", "l", "n")),
    ("z_2", ("1", blank, blank)): ("z_2", (blank, "1", blank), ("l", "l", "n")),
    ("z_2", ("#", blank, blank)): ("z_3", (blank, blank, blank), ("n", "r", "n")),

    ("z_3", (blank, "0", blank)): ("z_3", (blank, "0", blank), ("n", "r", "n")),
    ("z_3", (blank, "1", blank)): ("z_3", (blank, "1", blank), ("n", "r", "n")),
    ("z_3", (blank, blank, blank)): ("z_add", (blank, blank, blank), ("l", "l", "n")),

    ("z_add", ("0", "0", blank)): ("z_add", ("0", "0", "0"), ("l", "l", "l")),
    ("z_add", ("0", "1", blank)): ("z_add", ("0", "1", "1"), ("l", "l", "l")),
    ("z_add", ("1", "0", blank)): ("z_add", ("1", "0", "1"), ("l", "l", "l")),
    ("z_add", ("1", "1", blank)): ("z_carry", ("1", "1", "0"), ("l", "l", "l")),
    ("z_add", (blank, "0", blank)): ("z_add", (blank, "0", "0"), ("l", "l", "l")),
    ("z_add", (blank, "1", blank)): ("z_add", (blank, "1", "1"), ("l", "l", "l")),
    ("z_add", ("0", blank, blank)): ("z_add", ("0", blank, "0"), ("l", "l", "l")),
    ("z_add", ("1", blank, blank)): ("z_add", ("1", blank, "1"), ("l", "l", "l")),

    ("z_carry", ("0", "0", blank)): ("z_add", ("0", "0", "1"), ("l", "l", "l")),
    ("z_carry", ("0", "1", blank)): ("z_carry", ("0", "1", "0"), ("l", "l", "l")),
    ("z_carry", ("1", "0", blank)): ("z_carry", ("1", "0", "0"), ("l", "l", "l")),
    ("z_carry", ("1", "1", blank)): ("z_carry", ("1", "1", "1"), ("l", "l", "l")),
    ("z_carry", (blank, "0", blank)): ("z_add", (blank, "0", "1"), ("l", "l", "l")),
    ("z_carry", (blank, "1", blank)): ("z_carry", (blank, "1", "0"), ("l", "l", "l")),
    ("z_carry", ("0", blank, blank)): ("z_add", ("0", blank, "1"), ("l", "l", "l")),
    ("z_carry", ("1", blank, blank)): ("z_carry", ("1", blank, "0"), ("l", "l", "l")),

    ("z_add", (blank, blank, blank)): ("z_end", (blank, blank, blank), ("n", "n", "n")),
    ("z_carry", (blank, blank, blank)): ("z_end", (blank, blank, "1"), ("l", "l", "l"))

}
