import matplotlib.pyplot as plt


def apply_rules(axiom, rules):
    return "".join(rules.get(c, c) for c in axiom)


def draw_tree(axiom, rules, angle, distance, iterations):
    x, y = [0], [-200]
    heading = [90]
    for _ in range(iterations):
        axiom = apply_rules(axiom, rules)
    for c in axiom:
        if c == "F":
            x.append(x[-1] + distance * plt.np.sin(heading[-1] * plt.np.pi / 180))
            y.append(y[-1] + distance * plt.np.cos(heading[-1] * plt.np.pi / 180))
        elif c == "+":
            heading.append(heading[-1] - angle)
        elif c == "-":
            heading.append(heading[-1] + angle)
        elif c == "[":
            heading.append(heading[-1])
        elif c == "]":
            heading.pop()
        plt.plot(x, y)
        plt.pause(0.01)
    plt.show()


rules = {"F": "FF+[+F-F-F]-[-F+F+F]"}
axiom = "F"
angle = 25
distance = 5
iterations = 5
draw_tree(axiom, rules, angle, distance, iterations)
