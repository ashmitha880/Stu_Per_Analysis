def rem_dup(list):

  n=len(list)
  i=0
  j=1
  while j<n:
    if list[j]==list[i]:
        j+=1
    else:
        list[i+1]=list[j]
        i+=1
        j+=1
  return i+1
list=[1,1,2,2,2,3,3,3,3,4]
print(rem_dup(list))

