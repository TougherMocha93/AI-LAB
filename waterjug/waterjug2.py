import threading

j1size = 4
j2size = 3
final = [3,3]
jug1 = []
jug2 = []
lock = threading.Lock()
status = True

def j1():
    global jug1
    with lock:
        jug1 = [1 for i in range(j1size)]
    return levels()

def j2():
    global jug2
    with lock:
        jug2 = [1 for _ in range(j2size)]
    return levels()

def fromj2toj1():
    global jug1, jug2

    with lock:
        while len(jug1) < j1size and len(jug2) > 0:
            jug1.append(1)
            jug2.pop()

    return levels()

def j1empty():
    global jug1
    jug1 = []
    return levels()

def j2empty():
    global jug2
    jug2 = []
    return levels()

def levels():
    return [len(jug1), len(jug2)]

def exec_():
    global jug1, status
    while status:
        if jug1 == [1, 1, 1, 1]:
            with lock:
                jug1 = []
                print(levels())
        elif levels() == final:
            print(levels())
            status = False
            break
        elif levels()[0] == final[1] and levels()[1] == final[0]:
            j2empty()
            print(levels())
        elif levels()[0] == j1size or final == [j1size,0]:
            j2empty()
            j1()
            status = False
            break
        elif final == [j1size,j2size]:
            j2()
            j1()
            status = False
            break
        else:
            j2()
            print(levels())
            fromj2toj1()
            print(levels())

def checker():
    global status
    while True:
        if levels() == final:
            print("found")
            print(levels())
            status = False
            break

t1 = threading.Thread(target=exec_)
t2 = threading.Thread(target=checker)

t2.start()
t1.start()

t2.join()
t1.join()