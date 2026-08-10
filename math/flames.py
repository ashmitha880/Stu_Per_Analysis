def flames(list1,list2):
    for i in len(list1):
        for j in len(list2):
           if(list1[i]==list2[j]):    
            list1.remove(list[i])
            list2.remove(list2[i])
           return(list1+"*"+list2,True)
    return(list1+"*"+list2,False)
def main():
   name1=input("enter the name of the 1st person : ").lower().replace(" ","")
   name2=input("enter the name of the 2nd person : ").lower().replace(" ","")
   list1=list(name1)
   list2=list(name2)
   proceed=True
   while proceed:
        result,proceed=flames(list1,list2)
   count=len(list1)+len(list2)
   result=["friends","love","affection","marriage","enemies","siblings"]
   split_index=(len(count)%len(result))-1
   if split_index>=0:
        right_list=result[split_index+1:]
        left_list=result[:split_index]
        new_result=right_list+left_list
   else:
       new_result=result[split_index:]
   while len(new_result>1):
        if split_index>=0:
            right_list=new_result[split_index+1:]
            left_list=new_result[:split_index]
            new_result=right_list+left_list
        else:
            new_result=result[split_index:]
          
   final_result=new_result[0]    
   