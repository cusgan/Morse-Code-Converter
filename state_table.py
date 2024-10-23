# This file contains the state transition table of the Morse Code converter.
# The transition table is stored as a dictionary.
# 0 index is dot (.) input, 1 index is dash (-) input

state_table = {
    "Start": [
        "E",
        "T"
    ],
    "E": [
        "I",
        "A"
    ],
    "T": [
        "N",
        "M"
    ],
    "I": [
        "S",
        "U"
    ],
    "A": [
        "R",
        "W"
    ],
    "N": [
        "D",
        "K"
    ],
    "M": [
        "G",
        "O"
    ],
    "S": [
        "H",
        "V"
    ],
    "U": [
        "F",
        "Dead"
    ],
    "R": [
        "L",
        "Dead"
    ],
    "W": [
        "P",
        "J"
    ],
    "D": [
        "B",
        "X"
    ],
    "K": [
        "C",
        "Y"
    ],
    "G": [
        "Z",
        "Q"
    ],
    "O": [
        "Dead",
        "Dead"
    ],
    "H": [
        "Dead",
        "Dead"
    ],
    "V": [
        "Dead",
        "Dead"
    ],
    "F": [
        "Dead",
        "Dead"
    ],
    "L": [
        "Dead",
        "Dead"
    ],
    "P": [
        "Dead",
        "Dead"
    ],
    "J": [
        "Dead",
        "Dead"
    ],
    "B": [
        "Dead",
        "Dead"
    ],
    "X": [
        "Dead",
        "Dead"
    ],
    "C": [
        "Dead",
        "Dead"
    ],
    "Y": [
        "Dead",
        "Dead"
    ],
    "Z": [
        "Dead",
        "Dead"
    ],
    "Q": [
        "Dead",
        "Dead"
    ],
    "Dead": [
        "Dead",
        "Dead"
    ]
}