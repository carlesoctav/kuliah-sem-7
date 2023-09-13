import sys
import random

sys.setrecursionlimit(10000)
get_atmost = 1000


def check_terminal(solutions, non_terminal_symbols):
    for i in solutions:
        if i in non_terminal_symbols:
            return False
    return True


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


def construct_language_bfs(
    terminal_symbols,
    non_terminal_symbols,
    start_symbol,
    productions,
    solutions="",
):
    language = set()
    queue = [solutions]
    while queue:
        solutions = queue.pop(0)

        if len(language) >= get_atmost:
            return language

        if solutions == "":
            solutions = start_symbol

        if check_terminal(solutions, non_terminal_symbols=non_terminal_symbols):
            language.add(solutions)

        for alpha, beta in productions:
            if alpha in solutions:
                queue.append(solutions.replace(alpha, beta, 1))


if __name__ == "__main__":
    terminal_symbols, non_terminals_symbols, start_symbol, productions = test_case_1()

    lang = construct_language_bfs(
        terminal_symbols,
        non_terminals_symbols,
        start_symbol,
        productions,
        solutions="",
    )

    print(f"==>> lang: {lang}")
