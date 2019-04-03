from sklearn.feature_extraction.text import TfidfVectorizer


S1="The car is driven on the road"
S2="The truck is driven on the highway"

tfidf=TfidfVectorizer()
response=tfidf.fit_transform([S1,S2])

feature_names = tfidf.get_feature_names()
for col in response.nonzero()[1]:
    print (feature_names[col], ' - ', response[0, col])