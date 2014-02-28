
#create the document list and the class list
def loadDataSet():
    postingList =['My dog has flea problems help please','maybe not take him to the dog park stupid','my dalmation is so cute I love him','stop posting stupid worthless garbage','mr licks ate my steak how to stop him','quit buying worthless dog food stupid']
    classVec = [0,1,0,1,0,1]
    return postingList,classVec

#get unique words from the documents.
def createVocabList(dataSet):
    vocabSet= set({})
    for posting in dataSet:
        vocabSet = vocabSet | set(posting.split(' '))
    return list(vocabSet)

#create a vector of 1s and 0s depicting if the word in vocabulary exists in the document or not.
def setOfWords2Vec(vocabList,inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]=1
    return returnVec

#given a word vector w, what is the probability that it belongs to class c?
# p(c/w) = p(w/c)*p(c)/p(w)=p(w0/c)*p(w1/c)...*p(wn/c)*p(c)/p(w)
# p(c) = number of words in a class/total number of words.
# p(w0/c) = number of w0 words in a class/total number of words in the class.
# in this case: c = whether it belongs to abusive or not.
def trainNB0(trainDocMatrix,trainCategoryVector):
    
