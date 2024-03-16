list=[12,42,23,96,7,18,10,133]
min=list[0]
max=list[0]
minid=0
maxid=0
for i in range (0,len(list)):
    #min
    if min>list[i]:
        min=list[i]
        minid=i
    #max
    if max<list[i]:
        max=list[i]
        maxid=i
sum=max+min
diff=max-min
list[maxid]=sum
list[minid]=diff
print(list)
    
            
