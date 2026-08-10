l1=list(map(float,input().split()))
l2=[]
for i in l1:
    i//=1
    l2.append(i)
l3=list(map(int,l2))
print(*l3,sep=",")