l=[str(i) for i in input().split()]
s1=l[0]
s2=l[1]
f=0
for i in range(0,len(s1)):
    if(s1[i]!=s2[i]):
        f=f+1
if(f>=2):
    print("no")
if(f==1):
    print("yes")
