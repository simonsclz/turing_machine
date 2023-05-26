# The alphabet, the machine should work on
alphabet = ["1", "0", "#"]

# Initial state
init_state = "z_0"

# End states
end_states = ["z_end"]

# All states, add "normal" states
states = [init_state] + end_states + ["sub_z_1", "sub_z_2", "sub_z_3", "z_sub", "sub_z_carry"]

# The blank
blank = "⃞"

# Number of tapes
tapes = 3

# If the machine should print its actions
print_actions = False

# Delta-/transition-function
delta = {
    ("z_0", ("0", blank, blank)): ("z_0", ("0", blank, blank), ("r", "r", "r")),
    ("z_0", ("1", blank, blank)): ("z_0", ("1", blank, blank), ("r", "r", "r")),
    ("z_0", ("#", blank, blank)): ("sub_z_1", ("#", blank, blank), ("r", "l", "l")),

    ("sub_z_1", ("0", blank, blank)): ("sub_z_1", ("0", blank, blank), ("r", "n", "n")),
    ("sub_z_1", ("1", blank, blank)): ("sub_z_1", ("1", blank, blank), ("r", "n", "n")),
    ("sub_z_1", (blank, blank, blank)): ("sub_z_2", (blank, blank, blank), ("l", "n", "n")),

    ("sub_z_2", ("0", blank, blank)): ("sub_z_2", (blank, "0", blank), ("l", "l", "n")),
    ("sub_z_2", ("1", blank, blank)): ("sub_z_2", (blank, "1", blank), ("l", "l", "n")),
    ("sub_z_2", ("#", blank, blank)): ("sub_z_3", (blank, blank, blank), ("n", "r", "n")),

    ("sub_z_3", (blank, "0", blank)): ("sub_z_3", (blank, "0", blank), ("n", "r", "n")),
    ("sub_z_3", (blank, "1", blank)): ("sub_z_3", (blank, "1", blank), ("n", "r", "n")),
    ("sub_z_3", (blank, blank, blank)): ("z_sub", (blank, blank, blank), ("l", "l", "n")),

    ("z_sub", ("0", "0", blank)): ("z_sub", ("0", "0", "0"), ("l", "l", "l")),
    ("z_sub", ("0", "1", blank)): ("sub_z_carry", ("0", "1", "1"), ("l", "l", "l")),
    ("z_sub", ("1", "0", blank)): ("z_sub", ("1", "0", "1"), ("l", "l", "l")),
    ("z_sub", ("1", "1", blank)): ("z_sub", ("1", "1", "0"), ("l", "l", "l")),
    ("z_sub", (blank, "0", blank)): ("z_sub", (blank, "0", "0"), ("l", "l", "l")),
    ("z_sub", (blank, "1", blank)): ("sub_z_carry", (blank, "1", "1"), ("l", "l", "l")),
    ("z_sub", ("0", blank, blank)): ("z_sub", ("0", blank, "0"), ("l", "l", "l")),
    ("z_sub", ("1", blank, blank)): ("z_sub", ("1", blank, "1"), ("l", "l", "l")),

    ("sub_z_carry", ("0", "0", blank)): ("sub_z_carry", ("0", "0", "1"), ("l", "l", "l")),
    ("sub_z_carry", ("0", "1", blank)): ("sub_z_carry", ("0", "1", "0"), ("l", "l", "l")),
    ("sub_z_carry", ("1", "0", blank)): ("z_sub", ("1", "0", "1"), ("l", "l", "l")),
    ("sub_z_carry", ("1", "1", blank)): ("sub_z_carry", ("1", "1", "1"), ("l", "l", "l")),
    ("sub_z_carry", (blank, "0", blank)): ("sub_z_carry", (blank, "0", "1"), ("l", "l", "l")),
    ("sub_z_carry", (blank, "1", blank)): ("sub_z_carry", (blank, "1", "0"), ("l", "l", "l")),
    ("sub_z_carry", ("0", blank, blank)): ("sub_z_carry", ("0", blank, "1"), ("l", "l", "l")),
    ("sub_z_carry", ("1", blank, blank)): ("z_sub", ("1", blank, "0"), ("l", "l", "l")),

    ("z_sub", (blank, blank, blank)): ("z_end", (blank, blank, blank), ("n", "n", "n")),
    ("sub_z_carry", (blank, blank, blank)): ("z_end", (blank, blank, "1"), ("l", "l", "l"))

}
