a=input("Enter a sentence::")
l=[]
n=0
j=0
for i in range(0,len(a)):
	if(a[i]==" "):	
		l.append(a[n:i])
		n=i
		j=i
l.append(a[j:len(a)])
for i in range(0,len(l)):
	if(i==" ."):
		del l[i]
print(l) 
