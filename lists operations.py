list1=[1,"abc","12a#"] #create list
print(list1)
print(list1[0:1])  # slicing list
print(list1[:2])
print(list1[::-1])  #reverse list
list1[0]="xyz"
print(list1)     #list update
list1[1]=[1,2,3,4]
print(list1)
list1.append(7)   #append
list1.insert(1,8)   #insert
print(list1)

               
for i in range (0,len(list1)):
    print(list1[i])
for i in range (0,len(list1)):
    print(list1[i],end=" ")
for i in range (0,len(list1)):
    print(list1[i],end=" ",sep=" # ")
list1.remove(8)

    
