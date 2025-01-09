class Library:
    def __init__(self):
        self.name=input("Enter book name : ")
        self.id = input("Enter id : ")
        self.marks = int(input("Enter marks : "))
database={}
a=True
i=0
while(a==True):
    i+=1
    l = Library()
    boo = 'name'+str(i)
    d={}
    d['name'] = l.name
    d['author'] = l.author
    d['genre'] = l.genre
    database[boo] = d
    choice  = input("Enter choice cont/stop : ")
    if (choice == 'stop'):
        a = False
print(database)