import numpy as np

def sizefloor(r,c):
    global floor
    floor = np.random.choice(["Clean","Dirt"],size = (r,c))

def dispfloor():
    for i in floor:
        print(i)

def signal(i,j):
    print(f"Cleaning {i},{j}")
    return "Clean"

def clean():
    global floor
    floor = [[signal(i1,i2) if v2 == "Dirt" else v2 for i2, v2 in enumerate(v1)] for i1, v1 in enumerate(floor)]
    print("Cleaning Complete")

sizefloor(3,3)
dispfloor()
clean()
dispfloor()