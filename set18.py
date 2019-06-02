s=str(input())
s=s.capitalize()
l=len(s)
for i in range(0,l-1):
    if(s[i]==' '):
        i=i+1
        s=s[:i]+s[i:].capitalize()
print(s)
