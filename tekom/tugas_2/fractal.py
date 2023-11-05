import turtle


def apply_rules(sentensial, productions):
    new_sentensial = ""
    for c in sentensial:
        if c in productions:
            new_sentensial += productions[c]
    return new_sentensial


def draw_tree(start_symbol, productions, angle, distance, iterations):
    sentensial = start_symbol
    stack = []
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.setheading(90)
    for _ in range(iterations):
        sentensial = apply_rules(sentensial, productions)

    sentensial = sentensial.replace("D", "d", -1)
    for c in sentensial:
        if c == "d":
            turtle.forward(distance)
        elif c == "+":
            turtle.right(angle)
        elif c == "-":
            turtle.left(angle)


productions = {"D": "D+D-D-DD+D+D-D", "S": "D+D+D+D", "+": "+", "-": "-"}
start_symbol = "S"
angle = 90
distance = 5
iterations = int(input())
draw_tree(start_symbol, productions, angle, distance, iterations)
turtle.done()
