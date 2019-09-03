checklist = list()

#create
def create(item):
    checklist.append(item)

#read
def read(index):
    return checklist[index]


#update
def update(index, item):
    checklist[index] = item

#remove
def destroy(index):
    checklist.pop(index)


def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1 

def mark_completed(index):
    update(index, '{} {}'.format('√', read(index)))


def mark_incomplete(index):
    update(index, '{}'.format(read(index))[1:])

def user_input(prompt):
    user_input = str.upper(input(prompt))
    return(user_input)

def select(function_code):
   # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = int(user_input("Index Number? "))

        # Remember that item_index must actually exist or our program will crash.
        print(read(item_index))

    # Print all items
    elif function_code == "P":
        list_all_items()
    
    # Update Item
    elif function_code == "U":
        item_index = int(user_input("Index number? "))
        input_item = user_input("What do you want to change it to? ")
        update(item_index, input_item)

    # Remove Item
    elif function_code == "D":
        item_index = int(user_input("Index number? "))
        destroy(item_index)
    
    #uncheck item
    elif function_code == "W":
        item_index = int(user_input("index Number? "))
        mark_incomplete(item_index)

    # Mark completed
    elif function_code == "F":
        item_index = int(user_input("Index Number? "))
        mark_completed(item_index)

    elif function_code == "Q":
        return False 

   

    # Catch all
    else:
        print("Unknown Option")

    return True

#testing
#def test():
    # create("purple sox")
    # create("red cloak")

    # print(read(0))
    # print(read(1))

    # update(0, "purple socks")
    # destroy(1)

    # print(read(0))

    # list_all_items()

    # mark_completed(0)

    # select("C")
    # # View the results
    # list_all_items()
    # # Call function with new value
    # select("R")
    # View results
    #list_all_items()
    # Continue until all code is run

    # select(input())

    # user_value = user_input("Please Enter a value:")
    # print(user_value)



running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, U to update item, D to remove item, F to mark as completed, W to unmark, and Q to quit:   ")
    running = select(selection)

        
        
#test()