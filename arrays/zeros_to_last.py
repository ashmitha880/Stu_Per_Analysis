#moving zeros in an array to last
def moving_zeros_to_last(arr):
    n=len(arr)
    for i in range(n):
        if arr[i]==0:
            j=i
            break
    for i in range(j+1,n):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
            i+=1
        else:
            i+=1
    return arr
arr=[1,0,2,0,0,3,4,0,6,7,0,7]
print(moving_zeros_to_last(arr))
