l=[x for x in range(2000,3201)]
l1=[x for x in l if (x%7==0 and x%5!=0)]
for i in l1:
	print(i,end=",")
