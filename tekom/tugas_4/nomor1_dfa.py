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
        dfa/nfa just a quintuple (Q, Σ, δ, q0, F)
        params:
            internal_state: list of internal state
            alphabet: list of alphabet
            transition_function: dict of transition function, see example for the difference between dfa and nfa.
            initial_state: initial state
            final_state: list of final state
            deterministic: is it a dfa or nfa

        example of transition function:
        # deterministic transition function
         det_trans_table =  {
             'q0': {
                 'a': 'q1',
                 'b': 'q2',
             },
         }
        # non-deterministic transition function
         non_det_trans_table = {
             'q0': {
                 'a': ['q1', 'q2'],
                 'b': ['q0'],
             },
         }

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


if __name__ == "__main__":
    transition_function = {
        "q0": {
            "a": "q1",
            "b": "q3",
        },
        "q1": {
            "a": "q2",
            "b": "q3",
        },
        "q2": {
            "a": "q4",
            "b": "q6",
        },
        "q3": {
            "a": "q1",
            "b": "q5",
        },
        "q4": {
            "a": "q4",
            "b": "q4",
        },
        "q5": {
            "a": "q9",
            "b": "q4",
        },
        "q6": {
            "a": "q2",
            "b": "q7",
        },
        "q7": {
            "a": "q8",
            "b": "q4",
        },
        "q8": {
            "a": "q4",
            "b": "q7",
        },
        "q9": {
            "a": "q10",
            "b": "q5",
        },
        "q10": {
            "a": "q4",
            "b": "q11",
        },
        "q11": {
            "a": "q10",
            "b": "q4",
        },
    }


    internal_state = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7","q8","q9","q10","q11"]
    final_state = ["q0", "q1", "q2", "q3", "q5", "q6", "q7","q8","q9","q10","q11"]

    dfa = Automata(
        internal_state= internal_state, 
        alphabet=["a", "b"],
        transition_function=transition_function,
        initial_state="q0",
        final_state= final_state,
        deterministic=True,
    )

    dfa.interactive_check_string()
