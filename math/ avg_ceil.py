import math
w=input().split()
l=list(w)
l2=[]
y=len(l2)
count=0
for i in l:
    x=len(i)
    l2.append(x)
mean=sum(l2)/len(l2)
new_mean=math.ceil(mean)
for j in l2:
    if j>new_mean:
        count+=1
print(count)