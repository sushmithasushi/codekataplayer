a=str(input())
l=len(a)
b=[]
for i in range(0,l):
	if(a[i].islower()==True):
	    b.append(a[i].upper())
	else:
		b.append(a[i].lower())
print(*b,sep='')
