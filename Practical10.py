#                              /////////////////////////// Practical -09 /////////////////////////////////

# Values
values = {
    1: 5,
    2: 8,
    3: 9,
    4: 8,
    5: 5
}


# Check whether the next value is better
def better(X):
    Y = X + 1

    if X in values and Y in values:
        if values[Y] > values[X]:
            return Y

    return None


# Hill Climbing Algorithm
def hill_climb(X):
    while True:
        Y = better(X)

        if Y is None:
            return X

        X = Y


# Function call
best = hill_climb(1)

print("Best Position:", best)
print("Maximum Value:", values[best])
