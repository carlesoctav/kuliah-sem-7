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
        dfa just a quintuple :D
        """

        self.internal_state = internal_state
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.initial_state = initial_state
        self.final_state = final_state
        self.deterministic = deterministic

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
        current_state = self.initial_state

        for char in string:
            if char not in self.alphabet:
                return False

            for q in queue:
                if char in self.transition_function[q]:
                    queue += self.transition_function[q][char]
                queue.remove(q)
        
        return any([q in self.final_state for q in queue])


# transition functio yang deterministic
# det_trans_table {
#     'q0': {
#         'a': 'q1',
#         'b': 'q2',
#     },

# }

# transition function yang non-deterministic
# non_det_trans_table = {
#     'q0': {
#         'a': ['q1', 'q2'],
#         'b': ['q0'],
#     },
# }


if __name__ == "__main__":
    transition_function = {
        'q0': {
            'a': 'q1',
            'b': 'q3',
        },
        'q1': {
            'a': 'q3',
            'b': 'q2',
        },
        'q2': {
            'a': 'q2',
            'b': 'q2',
        },
        'q3': {
            'a': 'q3',
            'b': 'q3',
        },
    }

    dfa = Automata(
        internal_state=['q0', 'q1', 'q2', 'q3'],
        alphabet=['a', 'b'],
        transition_function=transition_function,
        initial_state='q0',
        final_state=['q2'],
        deterministic=True,
    )

    print(dfa.check_string("abaaabbb")) # harusnya true
    print(dfa.check_string("aaabbb")) # harusnya false