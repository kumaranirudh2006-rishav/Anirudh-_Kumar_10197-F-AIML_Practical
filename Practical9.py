#                              //////////////////////// Practical - 08 //////////////////////////

# Edges: (Start, Next, Cost)
edges = [
    ("a", "b", 5),
    ("a", "c", 4),
    ("b", "d", 3),
    ("c", "d", 1),
    ("d", "e", 2)
]

# Heuristic values
h = {
    "a": 7,
    "b": 5,
    "c": 3,
    "d": 2,
    "e": 0
}


def astar(start, goal):
    # (f, g, current_node, path)
    open_list = [(0, 0, start, [start])]
    visited = set()

    while open_list:
        open_list.sort(key=lambda item: item[0])

        f, g, node, path = open_list.pop(0)

        if node == goal:
            return path, g

        if node in visited:
            continue

        visited.add(node)

        for source, next_node, cost in edges:
            if source == node and next_node not in visited:
                new_g = g + cost
                new_f = new_g + h[next_node]

                open_list.append(
                    (new_f, new_g, next_node, path + [next_node])
                )

    return None, None


# Function call
path, cost = astar("a", "e")

if path:
    print("Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("Path not found")
