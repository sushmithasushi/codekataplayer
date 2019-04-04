a=str(input())
b=[]
l=len(a)
for i in range(0,l):
    c=ord(a[i])
    c=c+3
    b.append(chr(c))
print(*b,sep='')
