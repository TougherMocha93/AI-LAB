def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()

    visited.add(start_node)
    print(start_node)

    for next in graph[start_node]:
        if next not in visited:
            dfs(graph, next, visited)


if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }

    node = 2

    print(f"Depth-First Traversal (starting from node {node}):")
    dfs(graph, node)