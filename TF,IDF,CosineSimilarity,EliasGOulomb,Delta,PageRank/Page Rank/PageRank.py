import numpy as np

print("Enter the nuber of rows and columns::")
a=int(input())
print("Enter the adjacency matrix(row wise)(in the form of a matrixi)::\n")

mat=np.zeros((a,a))
for i in range(a):
	mat[i]=input().split(" ")

print("\nThe entry is::\n")
print(mat)

print("\nEnter the number of iterations::\n")
n=int(input())

print("\nEnter the dumping factor::\n")
m=float(input())

for i in range(a):
	flag=1
	for j in range(a):
		if(mat[i,j]!=0):
			flag=0
	if flag==1:
		for j in range(a):
			mat[i,j]=1

print("\nThe adjacency matrix is::\n")
print(mat)		
			
for i in range(a):
	count=0
	for j in range(a):
		if(mat[i,j]==1):
			count+=1
	for j in range(a):
		if(mat[i,j]==1):
			mat[i,j]/=count

print("\nThe schotastic matrix is::\n")
print(mat)

B=mat.transpose()
print("\nThe transpose Schotastic matrix is::\n")
print(B)
print("\nThe matrix C is::\n")
C=(1.0-m)*(1/a)+(m)*B

print(C)

print("\nThe initial value of P is::\n")
P=np.array([[1],[1],[1],[1],[1]]);
print(P)

for i in range(n):
	P=np.dot(C,P)
	print("\nThe ranks in iteration ",i+1,"are::\n")
	print(P)




