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
print(l) 
x=[]
n=0
j=0
s=[]
for i in range(0,len(a)):
	if(a[i]==" "):
		x.append(a[n:i])
		n=i
		j=i
x.append(a[j:len(a)])
for i in x:
	if(i in s):
		continue
	else:
		s.append(i)
		print(i,x.count(i))
