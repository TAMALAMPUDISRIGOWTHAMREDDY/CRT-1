# write a program to check the on road price of a bike under the
#conditins if price is greater than 72000 then incometax is 10% of original price insurance will be 15% of the actual price
#2nd condition if price>1,50,000 and less than 2,00,000 then tax would be 25% and insurance will be 20%
# if price >2,00,000 then tax will be 35% and insurance will be 28%
#other wise min price starts from 72000 enter aa valid value.
#actualprice+tax+insurance=onroad price
price=int(input())
incometax=0
insurance=0
onroadprice=0
if price>72000:
    incometax=10/100*price
    insurance=15/100*price
    onroadprice=price+incometax+insurance
    print(onroadprice)
elif price>150000 and price<=200000:
    incometax=25/100*price
    insurance=20/100*price
    onroadprice=price+incometax+insurance
    print(onroadprice)
elif price>200000:
    incometax=35/100*price
    insurance=28/100*price
    onroadprice=price+incometax+insurance
    print(onroadprice)
else:
    print("min price starts from 72000 enter aa valid value.")
