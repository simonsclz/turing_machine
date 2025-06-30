# NAME: dict.turing
# DESCR: Find a v_i s.t. k = k_i for an input k[k_1:v_1; k_2:v_2; ...]

from Utils.TuringString import TuringString

# The alphabet, the machine should work on
alphabet = ["[", "]", "0", "1", ";", ":"]

# Initial state
init_state = "z_0"

# End states
end_states = ["z_end"]

# All states, add "normal" states
states = [init_state] + end_states + ["copy", "go_left", "parse", "get_value",
                                      "to_next_key", "go_left_parsing"]

# The blank
blank = "⃞"

# Number of tapes
tapes = 3

# If the machine should print its actions
print_actions = True

# Moving options
r = "r"
l = "l"
n = "n"

# Delta-/transition-function
delta = {
    ("z_0", ("1", blank, blank)): ("copy", (blank, "1", blank), (r, r, n)),
    ("z_0", ("0", blank, blank)): ("copy", (blank, "0", blank), (r, r, n)),

    # Copies the key k to the second tape
    ("copy", ("1", blank, blank)): ("copy", (blank, "1", blank), (r, r, n)),
    ("copy", ("0", blank, blank)): ("copy", (blank, "0", blank), (r, r, n)),

    # Moves the header of the second tape to the first character while maintaining the others
    ("copy", ("[", blank, blank)): ("go_left", ("[", blank, blank), (n, l, n)),
    ("go_left", ("[", "0", blank)): ("go_left", ("[", "0", blank), (n, l, n)),
    ("go_left", ("[", "1", blank)): ("go_left", ("[", "1", blank), (n, l, n)),
    ("go_left", ("[", blank, blank)): ("parse", ("[", blank, blank), (r, r, n)),
    ("go_left", (";", "0", blank)): ("go_left", (";", "0", blank), (n, l, n)),
    ("go_left", (";", "1", blank)): ("go_left", (";", "1", blank), (n, l, n)),
    ("go_left", (";", blank, blank)): ("parse", (";", blank, blank), (r, r, n)),

    # Parses a key k_i to the given key k
    ("parse", ("0", "0", blank)): ("parse", ("0", "0", blank), (r, r, n)),
    ("parse", ("1", "1", blank)): ("parse", ("1", "1", blank), (r, r, n)),
    ("parse", (":", blank, blank)): ("get_value", (":", blank, blank), (r, n, n)),  # key found
    ("parse", (":", "1", blank)): ("to_next_key", (":", "1", blank), (r, n, n)),
    ("parse", (":", "0", blank)): ("to_next_key", (":", "0", blank), (r, n, n)),
    ("parse", ("1", blank, blank)): ("to_next_key", ("1", blank, blank), (r, n, n)),
    ("parse", ("0", blank, blank)): ("to_next_key", ("0", blank, blank), (r, n, n)),
    ("parse", ("1", "0", blank)): ("to_next_key", ("1", "0", blank), (r, n, n)),
    ("parse", ("0", "1", blank)): ("to_next_key", ("0", "1", blank), (r, n, n)),

    # Moves the header of the first tape to the next key while maintaining the others
    ("to_next_key", ("1", blank, blank)): ("to_next_key", ("1", blank, blank), (r, n, n)),
    ("to_next_key", ("0", blank, blank)): ("to_next_key", ("0", blank, blank), (r, n, n)),
    ("to_next_key", (":", blank, blank)): ("to_next_key", (":", blank, blank), (r, n, n)),
    ("to_next_key", ("1", "0", blank)): ("to_next_key", ("1", "0", blank), (r, n, n)),
    ("to_next_key", ("0", "0", blank)): ("to_next_key", ("0", "0", blank), (r, n, n)),
    ("to_next_key", (":", "0", blank)): ("to_next_key", (":", "0", blank), (r, n, n)),
    ("to_next_key", ("1", "1", blank)): ("to_next_key", ("1", "1", blank), (r, n, n)),
    ("to_next_key", ("0", "1", blank)): ("to_next_key", ("0", "1", blank), (r, n, n)),
    ("to_next_key", (":", "1", blank)): ("to_next_key", (":", "1", blank), (r, n, n)),
    ("to_next_key", (";", "0", blank)): ("go_left", (";", "0", blank), (n, l, n)),
    ("to_next_key", (";", "1", blank)): ("go_left", (";", "1", blank), (n, l, n)),
    ("to_next_key", (";", blank, blank)): ("go_left", (";", blank, blank), (n, l, n)),

    # Extracts the value of a key k_i and copies it to the third tape
    ("get_value", ("0", blank, blank)): ("get_value", ("0", blank, "0"), (r, n, r)),
    ("get_value", ("1", blank, blank)): ("get_value", ("1", blank, "1"), (r, n, r)),
    ("get_value", (";", blank, blank)): ("z_end", (";", blank, blank), (n, n, n)),
    ("get_value", ("]", blank, blank)): ("z_end", ("]", blank, blank), (n, n, n))
}
