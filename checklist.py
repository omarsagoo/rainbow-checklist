print("hello world!")

checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)

#create
def create(item):
    checklist.append(item)

#read
def read(index):
    return checklist[index]

checklist = ['Blue', 'Orange']
checklist[1] = 'Cats'
print(checklist)

#update
def update(index, item):
    checklist[index] = item
