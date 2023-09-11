import sys
import random

sys.setrecursionlimit(10000)

language = set()
get_atmost = 3


def check_terminal(solutions, non_terminal_symbols):
    for i in solutions:
        if i in non_terminal_symbols:
            return False
    return True


def reorder_productions(
    productions,
    terminal_symbols,
    non_terminal_symbols,
):
    tier_1_productions = []
    tier_2_productions = []
    tier_3_productions = []
    tier_4_productions = []
    new_productions = []

    for alpha, beta in productions:
        beta_counter = [beta.count(i) for i in terminal_symbols]
        alpha_counter = [alpha.count(i) for i in terminal_symbols]

        if check_terminal(beta, non_terminal_symbols):
            tier_1_productions.append((alpha, beta))
        elif sum(beta_counter) > sum(alpha_counter) and alpha != "S":
            tier_2_productions.append((alpha, beta))
        elif alpha == "S":
            tier_3_productions.append((alpha, beta))
        else:
            tier_4_productions.append((alpha, beta))

    new_productions.append(tier_1_productions)
    new_productions.append(tier_2_productions)
    new_productions.append(tier_3_productions)
    new_productions.append(tier_4_productions)

    return new_productions


def construct_grammar(
    terminal_symbols: list,
    non_terminal_symbols: list,
    start_symbol: str,
    productions: list[list[tuple]],
    solutions="",
):
    global language, get_atmost

    if len(language) >= get_atmost:
        return None

    if solutions == "":
        solutions = start_symbol

    if check_terminal(solutions, non_terminal_symbols=non_terminal_symbols):
        language.add(solutions)
        return None

    for tier in productions:
        for i in range(3 * len(tier)):
            alpha, beta = random.choice(tier)
            if alpha in solutions:
                construct_grammar(
                    terminal_symbols,
                    non_terminal_symbols,
                    start_symbol,
                    productions,
                    solutions.replace(alpha, beta, 1),
                )


def test_case_1():
    terminal_symbols = ["a", "b"]
    non_terminals_symbols = ["A", "S"]
    start_symbol = "S"
    productions = [("S", "aAa"), ("A", "aAa"), ("A", "b")]

    return terminal_symbols, non_terminals_symbols, start_symbol, productions


def test_case_2():
    terminal_symbols = ["a", "b"]
    non_terminals_symbols = ["S", "B", "C"]
    start_symbol = "S"
    productions = [
        ("S", "aS"),
        ("S", "aB"),
        ("B", "bC"),
        ("C", "aC"),
        ("C", "a"),
    ]

    return terminal_symbols, non_terminals_symbols, start_symbol, productions


def test_case_3():
    terminal_symbols = ["a", "b", "c"]
    non_terminals_symbols = ["S", "A", "B", "C"]
    start_symbol = "S"
    productions = [
        ("bB", "bb"),
        ("bC", "bc"),
        ("cC", "cc"),
        ("cA", "caA"),
        ("S", "abC"),
        ("S", "aSBC"),
        ("CB", "BC"),
    ]

    return terminal_symbols, non_terminals_symbols, start_symbol, productions


if __name__ == "__main__":
    terminal_symbols, non_terminals_symbols, start_symbol, productions = test_case_3()

    productions = reorder_productions(
        productions, terminal_symbols, non_terminals_symbols
    )

    print(f"==>> productions: {productions}")

    construct_grammar(
        terminal_symbols,
        non_terminals_symbols,
        start_symbol,
        productions,
        solutions="",
    )

    print(language)
