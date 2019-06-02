import math
no=[int(i) for i in input().split()]
p=[]
for i in range(2,no[1]+1):
    p.append(i)
i=2
while(i<=int(math.sqrt(no[1]))):
    if i in p:
        for j in range(i*2,no[1]+1,i):
            if j in p:
                p.remove(j)
    i=i+1
a=[]
for i in p:
    if(i>=no[0]):
        a.append(i)
print(len(a))
