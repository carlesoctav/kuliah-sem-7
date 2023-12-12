from typing import List, Tuple

BLANK_SPACE = 10 # number of blank space added to the left and right of the tape.
MAX_ITER = 1_000_000 # maximum iteration to check if the turing machine is in infinite loop 

class TuringMachine:
    def __init__(
            self,
            internal_state:List[str],
            alphabet:List[str],
            tape_alphabet:List[str],
            transition_function:dict,
            initial_state:str,
            final_state:str,
            blank_symbol = "B",
    ):
        
        self.internal_state = internal_state
        self.alphabet = alphabet
        self.tape_alphabet = tape_alphabet
        self.transition_function = transition_function
        self.initial_state = initial_state
        self.blank_symbol = blank_symbol
        self.final_state = final_state
    
    def interactive_check_string(self):
        while True:
            string = input("Masukkan string (ketik 'exit' untuk keluar): ")
            if string == "exit":
                break

            is_accepted, tape = self.check_string(string)
            if is_accepted:
                print("String diterima")
                print(f"tape akhir: {tape}")
            else:
                print("String ditolak")
                print(f"tape akhir: {tape}")

    def make_bigger_tape(self, tape, pointer):
        if pointer < 0:
            tape = [self.blank_symbol] * BLANK_SPACE + tape
            pointer += BLANK_SPACE
            print(f"Pointer is less than 0, adding {BLANK_SPACE} blank space to the left")
        else:
            tape = tape + [self.blank_symbol] * BLANK_SPACE
            print(f"Pointer is more than {len(tape)}, adding {BLANK_SPACE} blank space to the right")
        return tape, pointer
    
    def remove_extra_blank(self, tape):
        if all([x == self.blank_symbol for x in tape]):
            return []

        while tape[0] == self.blank_symbol:
            tape = tape[1:]
        while tape[-1] == self.blank_symbol:
            tape = tape[:-1]
        return tape

    def check_string(self, string:str) -> Tuple[bool, str]:
        iter_counter = 0
        tape = [self.blank_symbol] * BLANK_SPACE + list(string) + [self.blank_symbol] * BLANK_SPACE
        pointer = BLANK_SPACE
        state = self.initial_state
        visited_state = set()
        while True:
            if state == self.final_state:
                return True, "".join(self.remove_extra_blank(tape))
            
            state_to_check_infinite_loop = (state, "".join(tape), pointer)
            
            if state_to_check_infinite_loop in visited_state:
                print("Infinite loop detected beacuse of repeated state, tape, and pointer configuration")
                return False, "".join(self.remove_extra_blank(tape))
            
            visited_state.add(state_to_check_infinite_loop)

            if iter_counter > MAX_ITER:
                print("Maximum iteration reached")
                return False, "".join(self.remove_extra_blank(tape))

            #halt if there's no transition
            if self.transition_function[state].get(tape[pointer]) is None:
                print("No transition for state {} and tape alphabet {}, halting".format(state, tape[pointer]))
                return False, "".join(self.remove_extra_blank(tape))
            
            state, change_tape, dpointer = self.transition_function[state][tape[pointer]]
            tape[pointer] = change_tape
            pointer += dpointer
            if pointer < 0 or pointer >= len(tape):
                tape, pointer = self.make_bigger_tape(tape, pointer)

            iter_counter += 1

    def test(self):
        test_cases_true = ['0'*(2**n) for n in range(10)]
        print(f"==>> test_cases_true: {test_cases_true}")
        test_cases_false = ['0'*(2**n+1) for n in range(1,10)]

        print("===automated test===")
        
        for test_case in test_cases_true:
            assert self.check_string(test_case)[0] == True, f"Test case {test_case} should be accepted"

        print("for test cases that should be rejected:")
        for test_case in test_cases_false:
            assert self.check_string(test_case)[0] == False, f"Test case {test_case} should be rejected"

        print("All test cases passed")
        print("===manual test===")

            
transition_function = {
    'q0': {
            '0': ('q1', 'B', 1),
    },
    'q1': {
            'x': ('q1', 'x', 1),
            '0': ('q2', 'x', 1),
            'B': ('q5', 'B', 1),
    },
    'q2': {
            'x': ('q2', 'x', 1),
            '0': ('q3', '0', 1),
            'B': ('q4', 'B', -1),
    },
    'q3': {
            'x': ('q3', 'x', 1),
            '0': ('q2', 'x', 1),
    },
    'q4': {
            '0': ('q4', '0', -1),
            'x': ('q4', 'x', -1),
            'B': ('q1', 'B', 1),
    },
}

turing_machine = TuringMachine(
    internal_state=['q0', 'q1', 'q2', 'q3', 'q4', 'q5'],
    alphabet=['0'],
    tape_alphabet=['0', 'x', 'B'],
    transition_function=transition_function,
    initial_state='q0',
    final_state='q5',
    blank_symbol='B',
)

turing_machine.test()
turing_machine.interactive_check_string()

