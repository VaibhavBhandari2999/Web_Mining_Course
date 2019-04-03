
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pandas import DataFrame
import re

n = input("Enter the para::")

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(n)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
	if w not in stop_words:
		filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)

s = []
l = []
h = []
for i in filtered_sentence:
	if (i in s):
		continue
	else:
		s.append(i)
		h.append(i)
		l.append(filtered_sentence.count(i))
		print(i, filtered_sentence.count(i))

print(h)
p = h
print(l)
q = len(h)
df = DataFrame({"Word": h, 'Frequency': l})
df.to_excel('Freq.xlsx', sheet_name='Sheet1', index=False)
' '.join(p)
print(p)

for i in range(len(l)):
	if l[i][0] == 'A' or 'S' or 'E':
		print(l[i], p[i])

'''
zczxc
for i in h:
    if(i==p.startswith('a')):
        print("A:",l[i])
        '''


'''
The proverb has deep meaning, which is always useful for a successful life. It conveys the
idea that we should always think and then act accordingly. Impulsive actions may lead us to
embarrassing and odd situations. As we should always think before we speak, in the same
way we should think before we act. Life is full of various factors, the factors which can fascinate
us for the moment but may lead us to failure or the factors which can repel immediately but
may be the stepping stones to success. For example, going to a movie or playing video games
may seem an attractive thing for the time being but can, in the course of time not only disturb
one’s studies but also injure our eyes. Therefore, we should always restrain our intuitive and
impulsive desires and then act according to what our mind says is right. Even the great men
like Gandhi. Nehru, John Kennedy have been prey to their passions and emotions due to
which the nations suffered. We should learn from their lives and should always act thoughtfully
'''
