from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pandas import DataFrame

n='The proverb has deep meaning, which is always useful for a successful life. It conveys the idea that we should always think and then act accordingly. Impulsive actions may lead us to embarrassing and odd situations. As we should always think before we speak, in the same way we should think before we act. Life is full of various factors, the factors which can fascinate us for the moment but may lead us to failure or the factors which can repel immediately but may be the stepping stones to success. For example, going to a movie or playing video games may seem an attractive thing for the time being but can, in the course of time not only disturb one’s studies but also injure our eyes. Therefore, we should always restrain our intuitive and impulsive desires and then act according to what our mind says is right. Even the great men like Gandhi. Nehru, John Kennedy have been prey to their passions and emotions due to which the nations suffered. We should learn from their lives and should always act thoughtfully.'

z = set(stopwords.words('english'))

x = word_tokenize(n)

x= [w for w in x if not w in z]

s=[]

for i in x:
    if(i==',' or i=='.' or i=="'"):
        continue
    else:
        s.append(i)
a=[]
b=[]
c=[]

for i in s:
	if (i in a):
		continue
	else:
		a.append(i)
		b.append(i)
		c.append(s.count(i))
		print(i, s.count(i))

print("\nFiltered para(unique words) without stopwords and tokenized is:")
print(b)            

m = DataFrame({"Word": b, 'Frequency': c})
m.to_excel('Freq_FAT.xlsx', sheet_name='Sheet1', index=False)

count=0

for i in b:
    if(i[0]=='a' or i[0]=='s' or i[0]=='e'):
        count+=1

print("\nThe number of letters starting with a,s or e is ::")
print(count)        

max1=0
for j in range(0,len(c)):
    if c[j]>max1:
        max1=j
    
        
print("\nThe maximum frequency word is::")
print(b[max1])
print(c[max1])

print('\nThe words starting with vowels are::')
for i in b:
    if i[0]=='a' or i[0]=='e' or i[0]=='i' or i[0]=='o' or i[0]=='u':
        print(i)

        
