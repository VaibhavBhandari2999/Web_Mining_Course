from collections import Counter
import pandas as pd

def computeTF(wordDict,bow):
    tfDict={}
    bowCount=len(bow)
    for word, count in wordDict.items():
        tfDict[word]=count/float(bowCount)
    return tfDict

def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))
    return idfDict

def computeTFIDF(tfBow,idfs):
    tfidf={}
    for word,val in tfBow.items():
        tfidf[word]=val*idfs[word]
    return tfidf

S1="Term frequency matrix is important for ranking docs."
S2="TFIDF is more important than Term frequency matrix for the same"

bowA=S1.split(" ")
bowB=S2.split(" ")

wordSet=set(bowA).union(set(bowB))
#print(wordSet)
#print()
wordDictA = dict.fromkeys(wordSet, 0) 
wordDictB = dict.fromkeys(wordSet, 0)
for word in bowA:
    wordDictA[word]+=1
   
for word in bowB:
    wordDictB[word]+=1
#print(wordDictA)
#print()
#print(wordDictB)
print()
print("The TF matrix is::")
print(pd.DataFrame([wordDictA,wordDictB]))

tfBowA=computeTF(wordDictA,bowA)
tfBowB=computeTF(wordDictB,bowB)

print()
print("The IDF values of each term::")
print(tfBowA)
print()
print(tfBowB)

idfs = computeIDF([wordDictA,wordDictB])

tfidfBowA = computeTFIDF(tfBowA, idfs)
tfidfBowB = computeTFIDF(tfBowB, idfs)

print()
print("The TF*IDF Matris::")
print(pd.DataFrame([tfidfBowA, tfidfBowB]))
