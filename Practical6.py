#                     /////////////////////////////// Practical - 06 /////////////////////////////////////


# Directional road connections
roads = [
    ("delhi", "agra"),
    ("agra", "gwalior"),
    ("gwalior", "bhopal"),
    ("delhi", "jaipur"),
    ("jaipur", "ajmer")
]


# Travel recommendation using recursion
def travel(X, Y, visited=None):
    if visited is None:
        visited = set()

    if X == Y:
        return [X]

    visited.add(X)

    for start, destination in roads:
        if start == X and destination not in visited:
            path = travel(destination, Y, visited.copy())

            if path:
                return [X] + path

    return None


# Function calls
print("Delhi to Bhopal:", travel("delhi", "bhopal"))
print("Delhi to Ajmer:", travel("delhi", "ajmer"))
print("Delhi to Mumbai:", travel("delhi", "mumbai"))
