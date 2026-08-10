#parametrised method
def summation(i,s):
    if i<1:
        print(s)
        return 
    return summation(i-1,s+i)
n=int(input("enter the num: "))
result=summation(n,0)
print(result)

#functional method
def summation(n):
    if n==0:
        return 0
    return n+summation(n-1)
n=int(input("enter the num: "))
print(summation(n))

