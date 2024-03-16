list=[2,0,1024,0,40,230,0]
list2=[]
for i in list:
    for j in range (len(list)):
        if i!=0:
            list[j]=i
            break        
        else:
            for k in range (len(list2)):
                list[len(list2)-k]=i
print(list)
                
            
        
    
        
        
        
    
        

        
