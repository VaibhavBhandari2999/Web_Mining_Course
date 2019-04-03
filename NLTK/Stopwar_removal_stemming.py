from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pandas import DataFrame
import re
n=input("Enter the sentence::")

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(n)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
        
print(word_tokens)
print(filtered_sentence)

s=[]
l=[]
h=[]
for i in filtered_sentence:
    if(i in s):
        continue
    else:
        s.append(i)
        h.append(i)
        l.append(filtered_sentence.count(i))
        print(i,filtered_sentence.count(i))

print(h)
p=h
print(l)
q=len(h)
df=DataFrame({"Word":h,'Frequency':l})
df.to_excel('Freq.xlsx',sheet_name='Sheet1',index=False)
' '.join(p)
print(p)

for i in range(len(l)):
    if(l[i][0]=='A' or 'B' or 'S' or 'D' or 'E'):
        print(l[i],p[i])

'''
zczxc
for i in h:
    if(i==p.startswith('a')):
        print("A:",l[i])
        '''
