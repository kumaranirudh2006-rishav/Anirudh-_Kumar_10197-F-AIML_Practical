#                      ///////////////////////////// Practical - 07 ///////////////////////////////


# Edges (connections)
edges = [
    ("a", "b"),
    ("a", "c"),
    ("b", "d"),
    ("b", "e"),
    ("c", "f"),
    ("e", "g")
]

# Heuristic values
h = {
    "b": 4,
    "c": 5,
    "d": 3,
    "e": 2,
    "f": 1,
    "g": 0
}


# Best First Search
def best_first(start, goal):
    path = [start]
    current = start
    visited = {start}

    while current != goal:
        # Find unvisited neighbors
        neighbors = [
            destination
            for source, destination in edges
            if source == current and destination not in visited
        ]

        if not neighbors:
            print("Goal not found!")
            return

        # Select neighbor with lowest heuristic
        next_node = min(neighbors, key=lambda node: h.get(node, float("inf")))

        path.append(next_node)
        visited.add(next_node)
        current = next_node

    print(" -> ".join(path))


# Function call
best_first("a", "g")
