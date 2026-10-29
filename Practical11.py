#                                 //////////////////////// Practical -10 ////////////////////////

from itertools import product

# Available colors
colors = ["red", "green", "blue"]


def diff(X, Y):
    return X != Y


def map_coloring():
    for A, B, C, D in product(colors, repeat=4):

        if (
            diff(A, B)
            and diff(A, C)
            and diff(C, D)
            and diff(B, D)
            and diff(B, C)
        ):
            print("A =", A)
            print("B =", B)
            print("C =", C)
            print("D =", D)
            return

    print("No solution found")


# Function call
map_coloring()
