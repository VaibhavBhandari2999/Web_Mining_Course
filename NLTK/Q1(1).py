a=input("Enter a sentence::")
l=[]
n=0
j=0
s=0
for i in range(0,len(a)):
	if(a[i]=="."):
		s=i
for i in range(0,s):
	if(a[i]==" "):
		l.append(a[n:i])
		n=i
		j=i
print(l) 
