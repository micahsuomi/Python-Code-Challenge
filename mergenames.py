names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
names3 = names1 + names2

unique_list = [] 

 # intilize a null list 
      
    # traverse for all elements 
for name in (names3): 
        # check if exists in unique_list or not 
    if name not in unique_list: 
        unique_list.append(name) 
    # print list 
    else:
        continue

print(unique_list)
#prints Ava, Emma, Olivia, Sophia




