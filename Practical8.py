#                       ////////////////////////////// Practical - 08 ////////////////////////////////


# Water Jug Problem
# Jug capacities: 4 litres and 3 litres
# Goal: (2, 0)

def move(state):
    A, B = state
    result = []

    # Fill 4-litre jug
    if A < 4:
        result.append((4, B))

    # Fill 3-litre jug
    if B < 3:
        result.append((A, 3))

    # Empty 4-litre jug
    if A > 0:
        result.append((0, B))

    # Empty 3-litre jug
    if B > 0:
        result.append((A, 0))

    # Pour 4-litre jug into 3-litre jug
    T = min(A, 3 - B)
    if T > 0:
        result.append((A - T, B + T))

    # Pour 3-litre jug into 4-litre jug
    T = min(B, 4 - A)
    if T > 0:
        result.append((A + T, B - T))

    return result


def path(state, visited=None):
    if visited is None:
        visited = set()

    # Goal state
    if state == (2, 0):
        return [state]

    visited.add(state)

    for next_state in move(state):
        if next_state not in visited:
            result = path(next_state, visited.copy())

            if result is not None:
                return [state] + result

    return None


# Start state
result = path((0, 0))

if result:
    for state in result:
        print(state)
else:
    print("No solution found")
