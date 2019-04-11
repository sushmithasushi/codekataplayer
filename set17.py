s=str(input())
st=""
for i in range(0,len(s)):
    if(len(s)%2==0):
        if(i%2==0):
            st+=s[i+1]
        else:
            st+=s[i-1]
    else:
        if(i<len(s)-1):
            if(i%2==0):
                st+=s[i+1]
            else:
                st+=s[i-1]
        else:
            st+=s[i]
print(st)
