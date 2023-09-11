import sys
import random

sys.setrecursionlimit(10000)

language = set()
get_atmost = 1000


def check_terminal(solutions, non_terminal_symbols):
    for i in solutions:
        if i in non_terminal_symbols:
            return False
    return True


def randomize_construct_grammar(
    terminal_symbols: list,
    non_terminal_symbols: list,
    start_symbol: str,
    productions: list[tuple],
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

    for i in range(3 * len(productions)):
        alpha, beta = random.choice(productions)
        if alpha in solutions:
            randomize_construct_grammar(
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
        ("S", "abC"),
        ("S", "aSBC"),
        ("CB", "BC"),
    ]

    return terminal_symbols, non_terminals_symbols, start_symbol, productions


if __name__ == "__main__":
    terminal_symbols, non_terminals_symbols, start_symbol, productions = test_case_2()

    randomize_construct_grammar(
        terminal_symbols=terminal_symbols,
        non_terminal_symbols=non_terminals_symbols,
        start_symbol=start_symbol,
        productions=productions,
    )
    print(language)
