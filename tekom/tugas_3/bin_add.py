# adjency list [(node, [(label, newnode, output), ...])] for binary addition
# nvm better use lookup table

lookup_tabel = {
    "N": {
        "00": ("N", "0"),
        "01": ("N", "1"),
        "10": ("N", "1"),
        "11": ("C", "0"),
    },
    "C": {
        "00": ("N", "1"),
        "01": ("C", "0"),
        "10": ("C", "0"),
        "11": ("C", "1"),
    },
}


def binary_addition(a: str, b: str) -> str:
    try:
        int(a, 2)
        int(b, 2)
    except ValueError:
        raise ValueError("Input must be binary")

    if "0b" in a:
        a = a[2:]
    if "0b" in b:
        b = b[2:]

    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    a = a[::-1]
    b = b[::-1]

    state = "N"
    sum = ""
    for x, y in zip(a, b):
        concat = f"{x}{y}"
        state, output = lookup_tabel[state][concat]
        sum += output

    if state == "C":
        sum += "1"
    sum = sum[::-1]

    return sum


if __name__ == "__main__":
    a = "1010000111001011"
    b = "10110001001"
    my_bin = binary_addition(a, b)
    print(f"==>> my_bin: {my_bin}")

    built_in_bin = bin((int(a, 2) + int(b, 2)))
    print(f"==>> built_in_bin: {built_in_bin}")

    assert my_bin == built_in_bin[2:]
