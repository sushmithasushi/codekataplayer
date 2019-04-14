n=str(input())
l=[]
for i in range(0,len(n)):
    l.append(n.count(n[i]))
t=l.index(max(l))
print(n[t])
