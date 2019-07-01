l=[str(i) for i in input().split()]
s1=l[0]
s2=l[1]
if(len(s1)!=len(s2)):
    print("no")
a1=[s1.count(ch) for ch in s1]
b1=[s2.count(ch) for ch in s2]
if(a1==b1):
    print("yes")
else:
    print("no")
