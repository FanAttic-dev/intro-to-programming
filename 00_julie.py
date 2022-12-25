import turtle

julie = turtle.Turtle()

h_init = 100
max_depth = 5


def go_back(h):
    julie.left(180)
    julie.forward(h)
    julie.left(180)


def make_branch(h):
    if h < h_init / max_depth:
        return

    # right branch
    julie.right(45)
    julie.forward(h)

    make_branch(h / 2)

    go_back(h)

    # left branch
    julie.left(90)
    julie.forward(h)

    make_branch(h / 2)

    go_back(h)
    julie.right(45)


julie.left(90)
julie.forward(h_init)
make_branch(h_init)

turtle.done()
