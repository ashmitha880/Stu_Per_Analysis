def name_print(name,count):
    if count==0:
        return 
    print(name)
    name_print(name,count-1)
name_print("Ash",5)
