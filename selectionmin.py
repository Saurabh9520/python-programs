list=[56,8,7,7,0,2]
print(list)
for i in range(len(list)-1):
    min_val=min(list[i:])
    min_ind=list.index(min_val,i)
    list[i],list[min_ind]=list[min_ind],list[i]
    print(list)
#print(list)                

    
