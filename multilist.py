booklet = [[1,2,3,4,5,6],[8,6,5,7,9],[6,5,4,3,2,1]]

def show_data():
    global booklet
    if len(booklet) > 0:
        print("Current Lists: \n")
        for i in range(len(booklet)):
            print(i,") ",booklet[i],"\n")
    else:
        print("There are no lists in the booklet! Add Lists to view them!")

def sort_list():
    global booklet
    selection = select_list()
    booklet[selection].sort()
    print("\nList Sorted!\n")

def comparison(booklet):
    selections = select_list_2()
    temp1 = [i for i in booklet[selections[0]]]
    temp1.sort()
    temp2 = [i for i in booklet[selections[1]]]
    temp2.sort()
    if temp1 == temp2:
        print("\nThe Lists are Same\n")
    else:
        print("\nThe Lists are not Same\n")

def select_list():
    global booklet
    if len(booklet) > 0:
        selection = int(input('Select List by Index Value: '))
        return selection
    else:
        print("There are no lists in the booklet! Add Lists to view them!")
    

def select_list_2():
    global booklet
    if len(booklet) > 0:
        selection1 = int(input('Select List 1 by Index Value: '))
        selection2 = int(input('Select List 2 by Index Value: '))
        return [selection1,selection2]
    else:
        print("There are no lists in the booklet! Add Lists to view them!")

def sum():
    global booklet
    selection = select_list()
    sum = 0
    for i in booklet[selection]:
        sum += int(i)
    print("The Sum of the list is: ",sum)

def add_list():
    global booklet
    templist = []
    print("Enter the values individually and type 'done' to add to booklet: ")
    while(1):
        val = input()
        if val != 'done':
            templist.append(int(val))
        else:
            break
    booklet.append(templist)
    print("\nAdded List to Booklet!\n")
        


def append_list():
    global booklet
    selections = select_list_2()
    final = booklet[selections[0]] + booklet[selections[1]]
    print("New List is: \n",final)
    print("\nAdded new list to Booklet\n")
    booklet.append(final)

def extend_list():
    global booklet
    selection = select_list()
    templist = []
    print("Enter the values individually and type 'done' to add to booklet: ")
    while(1):
        val = input()
        if val != 'done':
            templist.append(int(val))
        else:
            break
    booklet[selection].extend(templist)
    print("List Extended!")


def main():
    print("Options:\n1)\tAdd List\n2)\tSum of Lists\n3)\tShow Data\n4)\tAppend List\n5)\tSort List\n6)\tCompare Lists\n7)\tExtend List\n0)\tExit")
    print("\n")
    while(1):
        
        opt = int(input('Choose an option: '))
        if opt == 0:
            exit()
        elif opt == 1:
            add_list()
        elif opt == 2:
            sum()
        elif opt == 3:
            show_data()
        elif opt == 4:
            append_list()
        elif opt == 5:
            sort_list()
        elif opt == 6:
            comparison(booklet)
        elif opt == 7:
            extend_list()
        else:
            print("Out of Bounds")

main()