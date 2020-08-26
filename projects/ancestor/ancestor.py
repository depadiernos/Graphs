from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for vertex_1, vertex_2 in ancestors:
        graph.add_vertex(vertex_1)
        graph.add_vertex(vertex_2)

    for vertex_1, vertex_2 in ancestors:
        graph.add_edge(vertex_1, vertex_2)

    earliest_ancestor = None

    longest_path = 1

    for vertex in graph.vertices:

        path = graph.dfs(vertex, starting_node)

        if path:
            print(path)

            if len(path) > longest_path:
                longest_path = len(path)
                earliest_ancestor = vertex

        elif not path and longest_path == 1:
            earliest_ancestor = -1

    return earliest_ancestor