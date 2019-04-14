from collections import deque
k,num=map(int,input().split())
l=[int(i) for i in input().split()]
l=deque(l)
l.rotate(num)
l=list(l)
print(*l,sep=' ')
