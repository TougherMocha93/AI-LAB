global jug1
global jug2

global fj1
global fj2

final = [0,2]

iterations = []

def j1():
    global jug1
    jug1 = [1 for i in range(4)]
    return levels()


def j2():
    global jug2
    jug2 = [1 for i in range(3)]
    return levels()

def fromj1toj2(type):
    global jug1
    global jug2

    if type == 1:
        while(len(jug2) < 3 and len(jug1) > 0):
            jug2.append(1)
            jug1.pop()
    else:
        while(len(jug2) < 3 and len(jug1) > 0):
            jug2.append(1)
            jug1.pop()
        jug1 = []
    return levels()

def fromj2toj1(type):
    global jug1
    global jug2

    if type == 1:
        while(len(jug1) < 4 and len(jug2) > 0):
            jug1.append(1)
            jug2.pop()
    else:
        while(len(jug1) < 4 and len(jug2) > 0):
            jug1.append(1)
            jug2.pop()
        jug2 = []
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
    return [len(jug1),len(jug2)]

def finalize():
    global fj1
    global fj2
    fj1 = jug1
    fj2 = jug2
    iterations.append(levels())
    print(iterations)
    return levels()

#type 1 - to fill
#type 2 - overflow


jug1 = []
jug2 = []

while not levels() == final:
    if j1() not in iterations:
        print(1)
        finalize()
    elif j2() not in iterations:
        print(2)
        finalize()
    elif fromj1toj2(0) not in iterations:
        print(3)
        finalize()
    elif fromj1toj2(1) not in iterations:
        print(4)
        finalize()
    elif fromj2toj1(0) not in iterations:
        print(5)
        finalize()
    elif fromj2toj1(1) not in iterations:
        print(6)
        finalize()
    elif j1empty() not in
    
print(levels())