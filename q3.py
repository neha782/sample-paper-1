n=input().split(",")
j=1
fact=1
for i in n:
	x=eval(i)
	while(j<=x):
		fact=fact*j
		j+=1
	print(fact,end=",")
		
	
