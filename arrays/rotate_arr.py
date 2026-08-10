def rotate_arr(arr):
    n=len(arr)
    temp=arr[0]
    for i in range(n-1):
       arr[i]=arr[i+1]
    arr[n-1]=temp
    return arr
arr=[1,2,3,4,5]
print(rotate_arr(arr))
#rotate array by n elements
def rotate_arr_by_n_elements(d,arr):
    n=len(arr)
    d=d%n
    temp=arr[0:d]
    for i in range(d,n):
        arr[i-d]=arr[i]
    for j in range(n-d,n):
        arr[j]=temp[j-(n-d)]
    return arr
d=int(input("enter the no.of places to rotate by : "))
arr=[1,2,3,4,5,6,7,8,9,10]
print(rotate_arr_by_n_elements(d,arr))
#using reverse of an array
def rotate_an_arr_using_reverse(d,arr):
    n=len(arr)


