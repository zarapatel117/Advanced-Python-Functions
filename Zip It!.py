s1= {1,2,3}
s2={'b','a','c'}
s3 = list (zip(s1,s2))
print(s3)

l1=[10,20,30,40]
l2=[100,200,300,400]
for x,y in zip(l1,l2[::-1]):
    print(x,y)
stocks=['KPI green','adani','infosys']
prices=[2000,1000,2050]
new_dict= {stocks:prices for stocks,
             prices in zip(stocks, prices)}
print (new_dict)  
