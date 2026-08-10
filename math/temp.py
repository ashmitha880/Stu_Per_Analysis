temp=list(map(int,input().split()))
result=[]
for i in range(len(temp)):
    if temp[i]>50:
        result.append(temp[i])
if len(result)==0:
    print(0)
else:
    print(" ".join(result))
