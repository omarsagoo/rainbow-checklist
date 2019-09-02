print("hello world!")

# checklist = list()
# checklist.append('Blue')
# print(checklist)
# checklist.append('Orange')
# print(checklist)

#create
def create(item):
    checklist.append(item)

#read
def read(index):
    return checklist[index]

# checklist = ['Blue', 'Orange']
# checklist[1] = 'Cats'
# print(checklist)

#update
def update(index, item):
    checklist[index] = item

#remove
def destroy(index):
    checklist.pop(index)

#testing
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(read(1))

test()