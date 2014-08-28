from sklearn.neighbors import *
from numpy import genfromtxt,zeros,savetxt,tile,where

def fileToMat(file,labelsPresent):
    labels=None
    fileData = genfromtxt(file,delimiter=',',skip_header=1,dtype="int")
    if labelsPresent:
        labels=fileData[:,0]
        fileData=fileData[:,1:]
    return fileData,labels

def testClassifier():
    data,labels = fileToMat("data/train.csv",True)
    normData,ranges, min = normalize(data)
    testPercent=0.1
    numTestVectors = int(testPercent*data.shape[0])
    for k in range(3,20,2):
        neigh = KNeighborsClassifier(n_neighbors=k,algorithm="ball_tree")
        neigh.fit(normData[numTestVectors:,],labels[numTestVectors:,])
        errorCount = 0.0
        for i in range(numTestVectors):
            classifiedLabel = neigh.predict(normData[i])
            if(classifiedLabel!=labels[i]):
                errorCount=errorCount+1.0
        print r'K:%d,Error Rate:%f'%(k,((errorCount/float(numTestVectors))*100))

#didn't work gave 66% error rate.
def normalize(data):
    min = data.min(0)
    max = data.max(0)
    ranges = max-min
    denominator = tile(ranges,(data.shape[0],1))
    normData = ((data-tile(min,(data.shape[0],1)))/denominator)
    return normData,ranges,min

def digitRecognizer():
    trainData,labels=fileToMat("data/train.csv",True)
    testData,trainLabels = fileToMat("data/test.csv",False)
    classifiedResult = zeros((testData.shape[0],2))
    neigh = KNeighborsClassifier(n_neighbors=3,)
    neigh.fit(trainData,labels)
    for i in range(testData.shape[0]):
        classifiedResult[i,0]=i+1
        classifiedResult[i,1]=neigh.predict(testData[i])
        print "%d "%(i+1)
    savetxt("testResult_sklearn_3.csv",classifiedResult,delimiter=',',fmt="%d,%d",header='ImageId,Label')

if __name__=="__main__":
    digitRecognizer()
