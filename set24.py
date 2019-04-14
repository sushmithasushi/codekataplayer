n=int(input())
s=str(input())

l=['a','e','i','o','u','A','E','I','O','U']
for i in s:
    if i in l:
        s=s.replace(i,'')
s=s[::-1]
print(s)
