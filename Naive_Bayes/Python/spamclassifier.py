import csv
import sys

def getVocabulary(line):
    vocabularyList = list(set(line.lower().split()))
    return [word for word in vocabularyList if len(word)>3]

wordFreq={}
def train():
    with open("../data/training.csv") as inputfile:
        content = csv.reader(inputfile,delimiter=',')
        for line in content:
            wordList = getVocabulary(line[0])
            for word in wordList:
                if word in wordFreq and line[1] in wordFreq[word]:
                    wordFreq[word][line[1]]=wordFreq[word][line[1]]+1
                else:
                    wordFreq[word]={}
                    wordFreq[word][line[1]]=1
        print wordFreq


def classProbability(class):
    #p(c)=(number of c/total number)

def wordConditionalProbability(word):
    #p(w/c) = p(WnC)/p(c)

# p(c/w)=((p(w/c)*p(c))/p(w))
def classify(line):
    wordList = getVocabulary(line)
    

train()
classify(sys.argv[1])    

