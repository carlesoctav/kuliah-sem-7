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
        dfa just a quintuple (Q, Sigma, delta, q0, F)
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

        print('final state: ', current_state)
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
        test_cases_true = ["abab", "aabb", "bbaa", "abbaa", "aabb", "abababab", "ab"]
        test_cases_false = ["aaa", "bbb", "abbb", "bbba", "abbbba", "aabbaa"]

        for test_case in test_cases_true:
            try:
                assert self.check_string(test_case) == True
            except AssertionError:
                print("Test failed for string: ", test_case)
                print("expected True, got False")
                return


        for test_case in test_cases_false:
            try:
                assert self.check_string(test_case) == False
            except AssertionError:
                print("Test failed for string: ", test_case)
                print("expected False, got True")
                return

        print("Test passed")



if __name__ == "__main__":
    transition_function = {
        "q0": {
            "a": ["q1"],
            "b": ["q3"],
        },
        "q1": {
            "a": ["q2"],
            "b": ["q3"],
        },
        "q2": {
            "a": [],
            "b": ["q5"],
        },
        "q3": {
            "a": ["q1"],
            "b": ["q4"],
        },
        "q4": {
            "a": ["q8"],
            "b": [],
        },
        "q5": {
            "a": [],
            "b": ["q6"],
        },
        "q6": {
            "a": ["q7"],
            "b": [],
        },
        "q7": {
            "a": [],
            "b": ["q6"],
        },
        "q8": {
            "a": ["q9"],
            "b": [],
        },
        "q9": {
            "a": [],
            "b": ["q10"],
        },
        "q10": {
            "a": ["q9"],
            "b": [],
        },
    }


    internal_state = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7","q8","q9","q10"]
    final_state = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7","q8","q9","q10"]

    dfa = Automata(
        internal_state= internal_state, 
        alphabet=["a", "b"],
        transition_function=transition_function,
        initial_state="q0",
        final_state= final_state,
        deterministic=False,
    )
    dfa.test()
    dfa.interactive_check_string()

