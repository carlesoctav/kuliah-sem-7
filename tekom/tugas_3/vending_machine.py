from typing import Iterable, Union
from dataclasses import dataclass
from collections import OrderedDict
import json
import pandas as pd


class LookupTable:
    def __init__(
        self,
        max_money: int,
        possible_money: Iterable[int],
        possible_products: Iterable[tuple[str, int]],
    ):
        self.max_money = max_money
        self.possible_money = possible_money
        self.possible_products = possible_products
        self.table = self._generate_lookup_table()

    def _generate_lookup_table(self):
        lookup_table = OrderedDict()

        for i in range(self.max_money):
            lookup_table[f"S{i}"] = OrderedDict()
            for money in self.possible_money:
                if i + money <= self.max_money:
                    lookup_table[f"S{i}"][money] = (f"S{i+money}", "n")
                else:
                    lookup_table[f"S{i}"][money] = (
                        f"S{self.max_money}",
                        f"{self.max_money - i}",
                    )

            for product in self.possible_products:
                if i >= product[1]:
                    lookup_table[f"S{i}"][product[0]] = (f"S{i-product[1]}", product[0])
                else:
                    lookup_table[f"S{i}"][product[0]] = (
                        f"S{i}",
                        f"n",
                    )

            lookup_table[f"S{i}"]["END"] = ("S0", f"{i}")

        lookup_table[f"S{self.max_money}"] = OrderedDict()
        for money in self.possible_money:
            lookup_table[f"S{self.max_money}"][money] = (
                f"S{self.max_money}",
                f"{money}",
            )
        for product in self.possible_products:
            lookup_table[f"S{self.max_money}"][product[0]] = (
                f"S{self.max_money - product[1]}",
                f"{product[0]}",
            )

        lookup_table[f"S{self.max_money}"]["END"] = (
            "S0",
            f"{self.max_money}",
        )

        return lookup_table

    def print_table(
        self,
    ):
        self.df = pd.DataFrame.from_dict(self.table, orient="index")
        print(self.df)

    def print_graph(self):
        raise NotImplementedError
        # not working :D
        # self.G = nx.DiGraph()
        # for state in self.table:
        #     self.G.add_node(state)
        #     for input in self.table[state]:
        #         self.G.add_edge(state, self.table[state][input][0], input=input)

        # nx.draw(self.G, with_labels=True, font_weight="bold")


def vending_machine(
    inputs: Iterable[Union[str, int]], lookup_table: LookupTable
) -> Iterable[Union[str, int]]:
    state = "S0"
    for input in inputs:
        state, output = lookup_table.table[state][input]
        yield state, output


if __name__ == "__main__":
    max_money = 30
    possible_money = [5, 10, 25]
    possible_products = [("A", 10), ("B", 15), ("C", 25)]
    lookup_table = LookupTable(max_money, possible_money, possible_products)

    with open("lookup_table.json", "w") as f:
        json.dump(lookup_table.table, f)

    inputs = [
        25,
        25,
        10,
        25,
        25,
        25,
        5,
        10,
        "A",
        "A",
        "A",
        "C",
        10,
        "C",
        "C",
        "C",
        10,
        25,
        "END",
    ]

    lookup_table.print_table()
    print(f"==>> inputs: {inputs}")
    print(
        f"==>> list(vending_machine(inputs, lookup_table)): {list(vending_machine(inputs, lookup_table))}"
    )
