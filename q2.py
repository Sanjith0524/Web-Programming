class Library:
    def __init__(self):
        self.name=input("Enter student name : ")
        self.id = input("Enter id : ")
        self.marks = int(input("Enter marks : "))
database={}
a=True
i=0
while(a==True):
    i+=1
    l = Library()
    name = l.name
    d={}
    d['id'] = l.id
    d['marks'] = l.marks
    database[name] = d
    choice  = input("Enter choice cont/stop : ")
    if (choice == 'stop'):
        a = False
l = []
lt = list(database.keys())
for j in lt:
    m = database[j]['marks']
    l.append([j,m])
marks = []
for j in l:
    marks.append(j[1])
marks.sort(reverse=True)
name=[]
for i in range(0,3):
    for j in l:
        if j[1] == marks[i]:
            name.append(j[0]) 
        else:
            continue
for i in range (0,3):
    print(f"name : {name[i]} id : {database[name[i]]['id']} marks : {database[name[i]]['marks']}")