def bs(arr,l,r,x):
    if l<=r:
        mid=(l+r)//2
        if arr[mid]==x:
            print("Yes")
            return
        elif arr[mid]>x:
            return bs(arr,l,mid-1,x)
        else:
            return bs(arr,mid+1,r,x)
    else:
        print("No")
        return
n,m=map(int,input().split())
l=[int(i) for i in input().split()]
bs(l,0,n-1,m)
