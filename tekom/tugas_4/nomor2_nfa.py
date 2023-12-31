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
    
    def test(self):
        test_cases_true = ["aa", "aaa", "bababaa", "bababaaa", "bb", "bbb", "ababb", "aaabbba"]
        test_cases_false = ["abab", "baba", "abbba", "abbababab", "abababba"]

        for test_case in test_cases_true:
            try:
                assert self.check_string(test_case) == True
            except AssertionError:
                print("Test failed for string: ", test_case)
                print("expected: True, got: False")
                return


        for test_case in test_cases_false:
            try:
                assert self.check_string(test_case) == False
            except AssertionError:
                print("Test failed for string: ", test_case)
                print("expected: False, got: True")
                return

        print("Test passed")



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
            'L': ['q1', 'q5', 'q9', 'q13'], 
        },
        'q1': {
            'a': ['q2'],
            'b': ['q4'],
        },
        'q2': {
            'a': ['q3'],
            'b': ['q4'],
        },
        'q3': {
            'a': ['q3'],
            'b': ['q3'],
        },
        'q4': {
            'a': ['q4'],
            'b': ['q4'],
        },
        'q5': {
            'a': ['q8'],
            'b': ['q6'],
        },
        'q6': {
            'a': ['q8'],
            'b': ['q7'],
        },
        'q7': {
            'a': ['q7'],
            'b': ['q7'],
        },
        'q8': {
            'a': ['q8'],
            'b': ['q8'],
        },

        'q9': {
            'a': ['q10'],
            'b': ['q12'],
        },

        'q10': {
            'a': ['q11'],
            'b': ['q12'],
        },

        'q11': {
            'a': ['q11'],
            'b': ['q9'],
        },

        'q12': {
            'a': ['q10'],
            'b': ['q12'],
        },

        'q13': {
            'b': ['q14'],
            'a': ['q16'],
        },

        'q14': {
            'b': ['q15'],
            'a': ['q16'],
        },

        'q15': {
            'b': ['q15'],
            'a': ['q13'],
        },

        'q16': {
            'b': ['q14'],
            'a': ['q16'],
        },

    }


    nfa = Automata(
        internal_state=['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7','q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15','q16'],
        alphabet=['a', 'b', 'L'],
        transition_function=transition_function1_2,
        initial_state='q0',
        final_state=['q3', 'q7', 'q11', 'q15'],
        deterministic=False,
    )
    nfa.test()
    nfa.interactive_check_string() #depannya haru ada L, contoh Laabb