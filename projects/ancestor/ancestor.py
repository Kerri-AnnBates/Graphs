from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # Create the graph
    tree = Graph()
    added = []

    # Add keys and edges
    for pair in ancestors:  # (2, 4)
        for item in pair:
            if item not in added:
                tree.add_vertex(item)
                added.append(item)

        tree.add_edge(pair[1], pair[0])

    # print(tree.vertices)
    visited = tree.bft(starting_node)
    # Get last node
    last_node = visited[-1]

    # node itself is the last node, it has no parents. return -1
    if last_node == starting_node:
        return -1

    return last_node


# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
#                   (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# print(earliest_ancestor(test_ancestors, 6))
