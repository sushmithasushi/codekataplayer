n,k=map(int,input().split())
l=[int(i) for i in input().split()]
li=[]
try:
    for i in range(n-k,n):
        li.append(l[i])
    for i in range(0,n-k):
        li.append(l[i])
    print(*li,sep=' ')
except:
    print(*l,sep=' ')
