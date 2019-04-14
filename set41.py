class s:
    def __init__(self):
        self.items=[]
    def push(self,data):
        if(data==')'):
            self.pop()
        else:
            self.items.append(data)
    def pop(self):
        self.items.pop()
    def is_empty(self):
        return self.items==[]
o=s()
l=str(input())


for i in range(0,len(l),1):
    o.push(l[i])

v=0
v=o.is_empty()
if(v==1):
    print("yes")
else:
    print("no")
