#selection sort
def ss(arr):
    n=len(arr)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
num=[2,9,4,1,45,23]
sorted_num=ss(num)
print("sorted array: ",sorted_num)

# bubble sort
def bs(arr):
    n=len(arr)
    for i in range(n-1):
        flag=0
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
               arr[j],arr[j+1]=arr[j+1],arr[j]
               flag=1
        if flag==0:
            break

    return arr
num=[2,9,4,1,45,23]
sorted_num=bs(num)
print("sorted array: ",sorted_num)

#insertion sort
def i_s(arr):
    n=len(arr)
    for i in range(n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    return arr
num=[2,9,4,1,45,23]
sorted_num=i_s(num)
print("sorted array: ",sorted_num)

#merge sort(dive and merge)
def merge(arr,low,mid,high):
    temp=[]
    left=low
    right=mid+1

    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1

    while(left<=mid):
         temp.append(arr[left])
         left+=1
    while(right<=high):
        temp.append(arr[right])
        right+=1

    for i in range(len(temp)):
        arr[low+i]=temp[i]
def ms(arr,low,high):
    
    if low>=high:
        return 
    mid=(low+high)//2

    ms(arr,low,mid)
    ms(arr,mid+1,high)
    merge(arr,low,mid,high)

arr = [6, 3, 8, 5, 2, 7, 1, 4]
ms(arr, 0, len(arr) - 1)
print(arr)   

# def partition(arr, low, high):
#     pivot = arr[low]

#     i = low
#     j = high

#     while i < j:

#         while i < high and arr[i] <= pivot:
#             i += 1

#         while j > low and arr[j] > pivot:
#             j -= 1

#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[low], arr[j] = arr[j], arr[low]

#     return j


# def qs(arr, low, high):

#     if low < high:

#         p = partition(arr, low, high)

#         qs(arr, low, p - 1)
#         qs(arr, p + 1, high)


# arr = [6, 3, 8, 5, 2, 7, 1, 4]

# qs(arr, 0, len(arr) - 1)

# print(arr)

#quick sort(take a pivot element)
def pivot_el(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while i<=high-1 and arr[i]<=pivot:
            i+=1
        while  j>=low+1 and arr[j]>=pivot:
            j-=1
        if i<j:
           arr[i],arr[j]=arr[j],arr[i]
        
    arr[j],arr[low]=arr[low],arr[j]
    return j
        
def qs(arr,low,high):
    if low<high:
        partition_index=pivot_el(arr,low,high)
        qs(arr,low,partition_index-1)
        qs(arr,partition_index+1,high)

arr = [6, 3, 8, 5, 2, 7, 1, 4]
qs(arr, 0, len(arr) - 1)
print(arr)   
      




