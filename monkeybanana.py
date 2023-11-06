#Consider a room of size 5x5
#the program doesn't account for the room's size
"""
    0 1 2 3 4
0   x x x x x
1   x x x x x
2   x x x x x
3   x x x x x
4   x x x x x
"""

grab_status,pick_status,climb_status = False,False,False

chair = [1,1]

pos = [3,1]

banana = [3,3]

def climb():
    global pos
    global chair
    global climb_status,grab_status
    if pos == chair and not grab_status:
        print("Climbed Chair")
        climb_status  = True
        return None
    else:
        print("Chair not present")
        return None

def interact():
    global grab_status
    global pos
    global chair
    if not grab_status and pos == chair:
        print("Chair Grabbed")
        grab_status = True
        return None
    elif grab_status:
        print("Chair Dropped")
        chair = pos
        grab_status = False
        return None
    else:
        print("Who are you?")

""""""
def moveto(to):
    global pos
    print(f"Position {pos}")
    while not pos == to:
        if pos[0] < to[0]:
            pos[0] += 1
        if pos[1] < to[1]:
            pos[1] += 1
        if pos[0] > to[0]:
            pos[0] -= 1
        if pos[1] > to[1]:
            pos[1] -= 1
        print(f"Moved to {pos}")
    print(f"Reached  {pos}")


def pick():
    global pos
    global banana
    global pick_status
    if pos == banana and climb_status:
        print("Banana Caught!!!!")
        pick_status = True
        exit()
    else:
        print("Banana unreachable")

# moveto() - to move to a point
# interact() - to interact with chair
# pick() - to reach banana
# climb() - to climb chair [ if chair is present ]
# variables: chair , pos (current position) , banana

if "__main__" == __name__:

    print(f"Init Position: {pos}")
    print(f"Chair: {chair}")
    print(f"Banana: {banana}\n")

    climb()
    moveto(chair)
    interact()
    moveto(banana)
    interact()
    print(f"\nChair: {chair}")
    pick()
    print("Climb Status: ",climb_status)
    climb()
    print("Climb Status: ",climb_status)
    pick()