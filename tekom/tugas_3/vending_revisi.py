# FSM untuk vending machine sederhana
from typing import Iterable, Union
import pandas as pd

lookup_table = {
    # state : {input : (new_state, output)}
    # s0: state when there's no coin yet
    # s1: state when there's 1 coin already
    # s2: state when there's 2 coins already
    # s3: state when there's 3 coins already
    # s4: state when there's 4 coins already
    # s5: state when there's 5 coins already
    # input: 1, E (kembalian), snack bar, air mineral, soft drink, chips
    # output: n (no output), 1, 2, 3, 4, 5, snack bar, air mineral, soft drink, chips
    # harga snack bar: 3 koin, air mineral: 2 koin, soft drink: 4 koin, chips: 5 koin
    "S0": {
        1: ("S1", "n"),
        "E": ("S0", "n"),
        "snack bar": ("S0", "n"),
        "air mineral": ("S0", "n"),
        "soft drink": ("S0", "n"),
        "chips": ("S0", "n"),
    },
    "S1": {
        1: ("S2", "n"),
        "E": ("S0", 1),
        "snack bar": ("S1", "n"),
        "air mineral": ("S1", "n"),
        "soft drink": ("S1", "n"),
        "chips": ("S1", "n"),
    },
    "S2": {
        1: ("S3", "n"),
        "E": ("S0", 2),
        "snack bar": ("S2", "n"),
        "air mineral": ("S0", "air mineral"),
        "soft drink": ("S2", "n"),
        "chips": ("S2", "n"),
    },
    "S3": {
        1: ("S4", "n"),
        "E": ("S0", 3),
        "snack bar": ("S0", "snack bar"),
        "air mineral": ("S1", "air mineral"),
        "soft drink": ("S3", "n"),
        "chips": ("S3", "n"),
    },
    "S4": {
        1: ("S5", "n"),
        "E": ("S0", 4),
        "snack bar": ("S1", "snack bar"),
        "air mineral": ("S2", "air mineral"),
        "soft drink": ("S0", "soft drink"),
        "chips": ("S4", "n"),
    },
    "S5": {
        1: ("S5", 1),
        "E": ("S0", 5),
        "snack bar": ("S2", "snack bar"),
        "air mineral": ("S3", "air mineral"),
        "soft drink": ("S1", "soft drink"),
        "chips": ("S0", "chips"),
    },
}


def vending_machine(input, state):
    state, output = lookup_table[state][input]
    return state, output


def print_table(lookup_table):
    df = pd.DataFrame(lookup_table)
    print(df)


if __name__ == "__main__":
    state = "S0"
    returned_item = []
    kembalian = 0
    while True:
        print("=====================================")
        print(f"anda di state {state} berikut adalah input yang memungkinan: ")
        for x in lookup_table[f"{state}"]:
            print(x)
        print("T untuk mengakhiri transaksi")
        print("=====================================")
        new_input = input("masukkan input:")

        if new_input.isdigit():
            new_input = int(new_input)

        if new_input in lookup_table[f"{state}"].keys():
            new_state, output = vending_machine(new_input, state)
            state = new_state

            if type(output) == int:
                kembalian += output
                print(f"anda mendapatkan {output} koin kembalian")
            elif output != "n":
                returned_item.append(output)
                print(f"anda mendapatkan {output}")

        elif new_input == "T":
            if state != "S0":
                kembalian += int(state[1])
            returned_item.append(kembalian)
            print(f"anda mendapatkan {returned_item}")
            break
        else:
            print("input tidak valid")
            continue
