def print_num(i,n):
    if i>n:
       return 
    else:
        print(i)
    print_num(i+1,n)
print_num(1,9)
def print_revnum(i,n):
    if i<1:
        return
    else:
        print(i)
    print_revnum(i-1,n)
print_revnum(3,3)
def print_num_bt(i,m):
    if i<1:
       return
    print_num_bt(i-1,m)
    print(i)
m=5
print_num_bt(m,m)
def print_revnum_bt(i,n):
    if i>n:
        return 
    print_revnum_bt(i+1,n)
    print(i)
i=3
n=15
print_revnum_bt(i,n)

        
