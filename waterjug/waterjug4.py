j1size = 4
j2size = 3
final = [2, 0]

jug1 = 0
jug2 = 0
visited = set()

def dfs(jug1, jug2, final, visited):
    if (jug1, jug2) in visited:
        return False
    visited.add((jug1, jug2))

    if [jug1, jug2] == final:
        return True

    if jug1 < j1size:
        if dfs(j1size, jug2, final, visited):
            return True

    if jug2 < j2size:
        if dfs(jug1, j2size, final, visited):
            return True

    if jug1 > 0:
        if dfs(0, jug2, final, visited):
            return True

    if jug2 > 0:
        if dfs(jug1, 0, final, visited):
            return True

    pour = min(jug1, j2size - jug2)
    if pour > 0:
        if dfs(jug1 - pour, jug2 + pour, final, visited):
            return True

    pour = min(jug2, j1size - jug1)
    if pour > 0:
        if dfs(jug1 + pour, jug2 - pour, final, visited):
            return True

    return False

if dfs(jug1, jug2, final, visited):
    print("Final state reached!")
else:
    print("Final state cannot be reached.")
