def waterjug(m=4, n=3, d=2):
    jug1 = 0
    jug2 = 0
    while jug1 != d and jug2 != d:
        if jug1 == 0:
            jug1 = m
        print(f"({jug1},{jug2})")
        transfer = min(jug1, n - jug2)
        jug1 -= transfer
        jug2 += transfer
        print(f"({jug1},{jug2})")
        if jug1 == d or jug2 == d:
            break
        if jug1 == 0:
            jug1 = m
            print(f"({jug1},{jug2})")
        if jug2 == n:
            jug2 = 0
            print(f"({jug1},{jug2})")
    return jug1 == d or jug2 == d
x = waterjug(4, 3, 2)
print(x)