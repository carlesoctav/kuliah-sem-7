from random import randint
from typing import List

class Automata:
    def __init__(
        self, 
        internal_state: List[str],
        alphabet: List[str],
        transition_function: dict,
        initial_state: str,
        final_state: List[str],
        deterministic: bool,
    ):
        """
        dfa just a quintuple :DL
        """

        self.internal_state = internal_state
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.initial_state = initial_state
        self.final_state = final_state
        self.deterministic = deterministic

    def interactive_check_string(self):
        """
        interactive check string
        """

        while True:
            string = input("Masukkan string (ketik 'exit' untuk keluar): ")
            if string == "exit":
                break

            if self.check_string(string):
                print("String diterima")

            else:
                print("String ditolak")



    def check_string(self, string: str) -> bool:
        """
        check if the string is accepted by the dfa
        """

        if self.deterministic:
            return self._check_string_dfa(string)
        else:
            return self._check_string_nfa(string)

    def _check_string_dfa(self, string: str) -> bool:
        """
        check if the string is accepted by the dfa
        """

        current_state = self.initial_state

        for char in string:
            if char not in self.alphabet:
                return False

            current_state = self.transition_function[current_state][char]

        return current_state in self.final_state
    
    
    def _check_string_nfa(self, string: str) -> bool:
        """
        check if the string is accepted by the nfa
        """

        queue = [self.initial_state]
        for char in string:
            if char not in self.alphabet:
                return False
            
            queue_with_L = []
            next_queue = []

            for q in queue:
                if 'L' in self.transition_function[q]:
                    queue_with_L+= self.transition_function[q]['L']

            queue+= queue_with_L

            for q in queue:
                if char in self.transition_function[q]:
                    next_queue+= self.transition_function[q][char]

            
            queue = next_queue

        print('reachable states: ', queue)
        return any([q in self.final_state for q in queue])



# transition functio yang deterministic
# det_trans_table {
#     'q0': {
#         'a': 'q1',
#         'b': 'q2',
#     },

# }


# non_det_trans_table = {
#     'q0': {
#         'a': ['q1', 'q2'],
#         'b': ['q0'],
#     },
# }


if __name__ == "__main__":
    transition_function1_2 = {
        'q0': {
            'a': ['q1', 'q4'],
            'b': ['q3'],
        },
        'q1': {
            'a': [],
            'b': ['q2', 'q3'],
        },
        'q2': {
            'a': ['q4'],
            'b': ['q3'],
        },
        'q3': {
            'a': ['q3'],
            'b': [],
        },
        'q4': {
            'a': ['q5'],
            'b': ['q6'],
        },
        'q5': {
            'a': ['q8'],
            'b': ['q6'],
        },
        'q6': {
            'a': [],
            'b': ['q7'],
        },
        'q7': {
            'a': [],
            'b': ['q8'],
        },
        'q8': {
            'a': ['q8'],
            'b': ['q8'],
        },
    }
    nfa = Automata(
        internal_state=['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7','q8'],
        alphabet=['a', 'b', 'L'],
        transition_function=transition_function1_2,
        initial_state='q0',
        final_state=['q0', 'q1', 'q2', 'q3', 'q5', 'q6', 'q7'],
        deterministic=False,
    )

    print(nfa.check_string("aaa")) 