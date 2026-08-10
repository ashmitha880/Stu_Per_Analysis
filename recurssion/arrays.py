#two poiter method
def rev_arr(arr,l,r):
    if l>=r:
        return arr
    else:
        arr[l],arr[r]=arr[r],arr[l]
        rev_arr(arr,l+1,r-1)
list=[1,2,3,4,5]
rev_arr(list,0,len(list)-1)
print(list)

#to check a palindrome (string)
def p_check(i,s,n):
    if i>=n/2:
        return True
    if s[i]!=s[n-i-1]:
        return False
    return p_check(i+1,s,n)
my_str="madam"
print(p_check(0,my_str,len(my_str)))

