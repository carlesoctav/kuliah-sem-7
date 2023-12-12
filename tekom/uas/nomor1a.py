from typing import List, Tuple
import copy
import random

LAMBDA = ""

class PushDownAutomata:
    def __init__(
        self,
        transition_function: dict,
        initial_state: str,
        initial_stack_symbol: str,
        final_state: set,
    ):
        self.transition_function = transition_function
        self.initial_state = initial_state
        self.initial_stack_symbol = initial_stack_symbol
        self.final_state = final_state
        self.EOF_string = False

    def interactive_check_string(self):
        while True:
            self.EOF_string = False
            string = input("Masukkan string (ketik 'exit' untuk keluar): ")
            if string == "exit":
                break

            is_accepted = self.check_string(string)
            if is_accepted:
                print("String diterima")
            else:
                print("String ditolak")

    def test(self,num_test: int):

        def rand_not_equal_to(n: int) -> int:
            while True:
                x = random.randint(1, 100)
                if x != n:
                    return x
        
        random_n_m = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(num_test)]
        test_cases_true = ["a" * n + "b" * m + "c" * (n + m) for n, m in random_n_m]
        test_cases_false = ["a" * n + "b" * m + "c" * (rand_not_equal_to(n+m)) for n, m in random_n_m]
        print("=== Automate Test ===")
        for test_case in test_cases_true:
            self.EOF_string = False
            assert self.check_string(test_case) == True, f"String {test_case} should be accepted"
        
        for test_case in test_cases_false:
            self.EOF_string = False
            assert self.check_string(test_case) == False, f"String {test_case} should be rejected"

        self.EOF_string = False
        print("All test cases passed")


    def check_string(self, string)->bool:
        def read_char(string: str) -> Tuple[str, str]:
            if len(string) > 0:
                next_char = string[0]
                string = string[1:]
            else:
                next_char = chr(3)
                
            if next_char == chr(3):
                self.EOF_string = True

            return next_char, string
            
        def unread_char(ch: str, string: str) -> str:
            if len(ch) == 0:
                return string

            if len(ch) != 1:
                raise Exception(2)
            
            return ch + string

        def match_top_stack(aStacktop: str, stack: List[str]) -> bool:
            return stack[-1] == aStacktop

        def get_transitions(state_id: str, stack: List[str]) -> List[Tuple[str, str]]:
            transition_list = []

            for (
                a_state_id,
                an_input_sym,
                a_stack_top,
            ) in self.transition_function.keys():
                if state_id == a_state_id and match_top_stack(a_stack_top, stack):
                    transition_list.append((an_input_sym, a_stack_top))

            return transition_list

        def pop_and_push(
            a_stack_top: str, push_on_stack: str, stack: List[str]
        ) -> List[str]:
            new_stack = stack[:]
            for x in a_stack_top:
                new_stack.pop()
            for x in push_on_stack[::-1]:
                new_stack.append(x)
            return new_stack

        curr_state = self.initial_state
        pda_stack = [self.initial_stack_symbol]

        # since this is non-deterministic, we need to explore all possible paths
        ID = [(curr_state, string, pda_stack)]

        while not len(ID) == 0:
            curr_state, string, pda_stack = ID.pop()
            # print((curr_state, string, pda_stack))

            c, string = read_char(string)

            if self.EOF_string and curr_state in self.final_state:
                return True

            string = unread_char(c, string)

            for an_input_sym, a_stack_top in get_transitions(curr_state, pda_stack):
                for to_state_id, push_on_stack in self.transition_function[
                    (curr_state, an_input_sym, a_stack_top)
                ]:
                    if an_input_sym == LAMBDA:
                        ID.append(
                            (
                                to_state_id,
                                copy.deepcopy(string),
                                pop_and_push(a_stack_top, push_on_stack, pda_stack),
                            )
                        )
                    else:
                        c, string = read_char(string)
                        if c == an_input_sym:
                            ID.append(
                                (
                                    to_state_id,
                                    copy.deepcopy(string),
                                    pop_and_push(a_stack_top, push_on_stack, pda_stack),
                                )
                            )
                        string = unread_char(c, string)

        return False


transition_function = {
    ('q0', 'a', 'z'): set([('q0', 'az')]),
    ('q0', 'a', 'a'): set([('q0', 'aa')]),
    ('q0', 'b', 'a'): set([('q1', 'ba')]),
    ('q1', 'b', 'b'): set([('q1', 'bb')]),
    ('q1', 'c', 'b'): set([('q2', '')]),
    ('q2', 'c', 'b'): set([('q2', '')]),
    ('q2', 'c', 'a'): set([('q3', '')]),
    ('q3', 'c', 'a'): set([('q3', '')]),
    ('q3', '', 'z'): set([('q4', 'z')]),
}

npda = PushDownAutomata(

    transition_function,
    'q0',
    'z',
    set(['q4']),
)

npda.test(100)
npda.interactive_check_string()

