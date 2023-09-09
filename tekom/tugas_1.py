language = set()
get_atmost = 10


# change recursive limit
import sys

sys.setrecursionlimit(10000)
import random


def check_terminal(solutions, non_terminal_symbols):
    for i in solutions:
        if i in non_terminal_symbols:
            return False
    return True


def prioritize_terminal(productions, non_terminal_symbols):
    new_productions = []
    for alpha, beta in productions:
        if check_terminal(beta, non_terminal_symbols=non_terminals_symbols):
            new_productions.append((alpha, beta))
    for alpha, beta in productions:
        if not check_terminal(beta, non_terminal_symbols=non_terminals_symbols):
            new_productions.append((alpha, beta))
    return new_productions


def construct_grammar(
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
    print(f"==>> solutions: {solutions}")
    print(f"==>> language: {language}")

    if check_terminal(solutions, non_terminal_symbols=non_terminal_symbols):
        language.add(solutions)
        return None

    for alpha, beta in productions:
        if alpha in solutions:
            construct_grammar(
                terminal_symbols,
                non_terminal_symbols,
                start_symbol,
                productions,
                solutions.replace(alpha, beta, 1),
            )


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

    print(f"==>> solutions: {solutions}")

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


if __name__ == "__main__":
    # nomor 1
    # terminal_symbols = ["a", "b"]
    # non_terminals_symbols = ["A", "S"]
    # start_symbol = "S"
    # productions = [("S", "aAa"), ("A", "aAa"), ("A", "b")]

    # nomor 2
    # terminal_symbols = ["a", "b"]
    # non_terminals_symbols = ["S", "B", "C"]
    # start_symbol = "S"
    # productions = [("S", "aS"), ("S", "aB"), ("B", "bC"), ("C", "aC"), ("C", "a")]

    # nomor 3
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

    productions = prioritize_terminal(
        productions, non_terminal_symbols=non_terminals_symbols
    )

    print(f"==>> productions: {productions}")
    construct_grammar(
        terminal_symbols=terminal_symbols,
        non_terminal_symbols=non_terminals_symbols,
        start_symbol=start_symbol,
        productions=productions,
    )
    print(language)
