#                               //////////////////////// Practical -12 ////////////////////////////


# Values
values = {
    1: 9,
    2: 4,
    3: 1,
    4: 6,
    5: 8
}


def anneal(X, T):
    if T == 0:
        return X

    Y = X + 1

    if Y not in values:
        return X

    V1 = values[X]
    V2 = values[Y]

    if V2 < V1:
        Next = Y
    else:
        Next = X

    return anneal(Next, T - 1)


# Function call
Best = anneal(1, 5)

print("Best Position:", Best)
print("Best Value:", values[Best])
