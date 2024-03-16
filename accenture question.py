#calculate the diff of sum of numbers that are div by 6 and not divisible by 6
#in the range of first 30 numbers
sum1=0
sum2=0
for i in range (1,31):
    if i%6==0:
        sum1=sum1+i
    else:
        sum2=sum2+i
sum2=sum2-sum1
print(sum2)
        
    
