rom_num={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
s=0
r=str(input())
for i in range(len(r)):
    if i>0 and rom_num[r[i]]>rom_num[r[i-1]]:
        s+=rom_num[r[i]]-2*rom_num[r[i-1]]
    else:
        s+=rom_num[r[i]]
print(s)
