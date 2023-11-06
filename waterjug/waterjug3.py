from collections import deque

def bfs(initial, final):
    visited = set()
    queue = deque([(initial, [])])

    while queue:
        current_state, path = queue.popleft()
        jug1, jug2 = current_state

        if current_state in visited:
            continue
        visited.add(current_state)

        if current_state == final:
            return path

        next_states = [
            ((j1size, jug2), "Fill jug1"),
            ((jug1, j2size), "Fill jug2"),
            ((0, jug2), "Empty jug1"),
            ((jug1, 0), "Empty jug2"),
            ((jug1 - min(jug1, j2size - jug2), jug2 + min(jug1, j2size - jug2)), "Pour jug1 to jug2"),
            ((jug1 + min(j1size - jug1, jug2), jug2 - min(j1size - jug1, jug2)), "Pour jug2 to jug1")
        ]

        for state, action in next_states:
            queue.append((state, path + [action]))

    return None

j1size = 4
j2size = 3
initial_state = (0, 0)
final_state = (2, 0)

solution = bfs(initial_state, final_state)

if solution:
    for step, action in enumerate(solution, start=1):
        print(f"Step {step}: {action}")
else:
    print("No solution found.")