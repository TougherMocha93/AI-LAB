from collections import defaultdict, deque

def bfs(graph, start_node):
    visited = set()
    queue = deque()

    visited.add(start_node)
    queue.append(start_node)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


if __name__ == "__main__":
    graph = defaultdict(list)
    graph[0] = [2,1]
    graph[1] = [0,3]
    graph[2] = [0]
    graph[3] = [1]

    node = 0 #Starting Node

    print(f"Breadth-First Traversal (starting from node {node}):")
    bfs(graph, node)
