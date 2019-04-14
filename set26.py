n=int(input())
l=[int(i) for i in input().split()]
for i in range(0,n):
    t=1
    for j in range(0,n):
        if(i==j):
            next
        else:
            if l[i]==l[j]:
                t+=1
    if(t>1):
        next
    else:
        print(l[i])
        break
