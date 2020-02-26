d=input().split(",")
c=50
h=30
for i in d:
	s=eval(i)
	q=((2*c*s)/h)**(1/2)
	print(int(q))
